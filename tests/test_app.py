import io
import sqlite3
from pathlib import Path

import pytest
from werkzeug.security import generate_password_hash

from app import create_app
from app.analyzer import analyze, validate_config

SAMPLE = (Path(__file__).parents[1] / 'examples/switch_sintetico.cfg').read_text()


@pytest.fixture
def app(tmp_path):
    app = create_app({'TESTING': True, 'DATABASE': str(tmp_path / 'test.sqlite'), 'SECRET_KEY': 'test-only'})
    with sqlite3.connect(app.config['DATABASE']) as db:
        for email in ['one@example.test', 'two@example.test']:
            db.execute('INSERT INTO users(email,password_hash) VALUES (?,?)', (email, generate_password_hash('Senha-de-teste-123')))
    return app


def post(client, path, data=None, **kwargs):
    client.get('/login')
    with client.session_transaction() as session:
        token = session['csrf']
    return client.post(path, data={**(data or {}), 'csrf': token}, **kwargs)


def login(client, email='one@example.test'):
    return post(client, '/login', {'email': email, 'password': 'Senha-de-teste-123'})


def start(client):
    login(client)
    post(client, '/clientes', {'name': 'Cliente teste', 'environment': 'Laboratório'})
    return post(client, '/analises/nova', {'client_id': '1', 'authorized': 'yes',
        'config_file': (io.BytesIO(SAMPLE.encode()), 'switch.cfg')})


def test_rules_and_inventory():
    inventory, findings = analyze(SAMPLE)
    assert inventory['hostname'] == 'SW-LAB-01'
    assert len(inventory['interfaces']) == 2
    assert {f['id'] for f in findings} == {f'NET-00{i}' for i in range(1, 7)}


def test_no_false_positive_for_explicit_safe_commands():
    text = SAMPLE.replace('transport input telnet ssh', 'transport input ssh').replace('ip http server', 'no ip http server').replace('switchport trunk allowed vlan all', 'switchport trunk allowed vlan 10')
    text += '\nntp server 192.0.2.1\nlogging host 192.0.2.2\nip ssh version 2\n'
    assert analyze(text)[1] == []


@pytest.mark.parametrize('line', ['username admin secret abc', 'enable secret 5 xyz', 'snmp-server community public RO', ' password abc', ' key-string abc'])
def test_secrets_rejected(line):
    with pytest.raises(ValueError, match='segredo'):
        validate_config(SAMPLE + '\n' + line)


@pytest.mark.parametrize('text', ['', 'not a config', '\x00' + SAMPLE])
def test_bad_format(text):
    with pytest.raises(ValueError):
        validate_config(text)


def test_login_csrf_and_headers(app):
    client = app.test_client()
    assert client.get('/').status_code == 302
    assert client.post('/login', data={'email': 'one@example.test'}).status_code == 400
    assert login(client).status_code == 302
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers['X-Frame-Options'] == 'DENY'
    assert b'Vis' in response.data


def test_wrong_password(app):
    c = app.test_client()
    response = post(c, '/login', {'email': 'one@example.test', 'password': 'wrong'})
    assert b'incorretos' in response.data
    assert c.get('/').status_code == 302


def test_end_to_end_review_and_revoke(app):
    c = app.test_client()
    assert start(c).location.endswith('/analises/1')
    assert c.get('/analises/1/relatorio').status_code == 403
    post(c, '/analises/1/liberar', {'reviewed': 'yes'})
    assert c.get('/analises/1/relatorio').status_code == 403
    for i in range(1, 7):
        post(c, f'/analises/1/achados/{i}', {'decision': 'Confirmado', 'note': 'Confirmado em laboratório sintético.'})
    post(c, '/analises/1/liberar', {'reviewed': 'yes'})
    assert c.get('/analises/1/relatorio').status_code == 200
    post(c, '/analises/1/achados/1', {'decision': 'Descartado', 'note': 'Reavaliação por nova evidência.'})
    assert c.get('/analises/1/relatorio').status_code == 403
    with sqlite3.connect(app.config['DATABASE']) as db:
        assert db.execute('SELECT COUNT(*) FROM events').fetchone()[0] == 9


def test_isolation(app):
    first, second = app.test_client(), app.test_client()
    start(first)
    login(second, 'two@example.test')
    for path in ['/analises/1', '/analises/1/relatorio']:
        assert second.get(path).status_code == 404
    assert post(second, '/analises/1/achados/1', {'decision': 'Confirmado', 'note': 'Tentativa'}).status_code == 404
    assert post(second, '/analises/1/excluir', {'confirmation': 'EXCLUIR'}).status_code == 404
    assert post(second, '/analises/nova', {'client_id': 1, 'authorized': 'yes', 'config_file': (io.BytesIO(SAMPLE.encode()), 'switch.cfg')}).status_code == 404


def test_validation_and_delete(app):
    c = app.test_client()
    start(c)
    response = post(c, '/analises/nova', {'client_id': 1, 'authorized': 'yes', 'config_file': (io.BytesIO(b'x' * (256 * 1024 + 1)), 'huge.cfg')})
    assert b'256 KB' in response.data
    response = post(c, '/analises/nova', {'client_id': 1, 'config_file': (io.BytesIO(SAMPLE.encode()), 'switch.cfg')})
    assert b'Confirme' in response.data
    post(c, '/analises/1/excluir', {'confirmation': 'wrong'})
    assert c.get('/analises/1').status_code == 200
    post(c, '/analises/1/excluir', {'confirmation': 'EXCLUIR'})
    assert c.get('/analises/1').status_code == 404
    with sqlite3.connect(app.config['DATABASE']) as db:
        assert db.execute('SELECT COUNT(*) FROM findings').fetchone()[0] == 0
        assert db.execute('SELECT COUNT(*) FROM events').fetchone()[0] == 0


def test_html_escaping_and_persistence(app):
    c = app.test_client()
    login(c)
    post(c, '/clientes', {'name': '<script>alert(1)</script>', 'environment': 'Lab'})
    response = c.get('/clientes')
    assert b'<script>' not in response.data
    assert b'&lt;script&gt;' in response.data
    new_app = create_app({'TESTING': True, 'DATABASE': app.config['DATABASE'], 'SECRET_KEY': 'test-only'})
    other = new_app.test_client()
    login(other)
    assert b'&lt;script&gt;' in other.get('/clientes').data
