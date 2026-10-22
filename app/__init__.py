"""Aplicação local de diagnóstico Netrunner OT."""
import functools
import json
import os
import secrets
import sqlite3
from pathlib import Path

import click
from flask import (Flask, abort, flash, g, redirect, render_template,
                   request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from .analyzer import analyze, validate_config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    secret_path = Path(app.instance_path) / 'secret.key'
    if not secret_path.exists():
        try:
            with secret_path.open('x') as stream:
                stream.write(secrets.token_hex(32))
            secret_path.chmod(0o600)
        except FileExistsError:
            pass
    app.config.from_mapping(
        SECRET_KEY=os.getenv('NETRUNNER_SECRET') or secret_path.read_text(),
        DATABASE=str(Path(app.instance_path) / 'netrunner.sqlite'),
        MAX_CONTENT_LENGTH=512 * 1024,
        SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=os.getenv('NETRUNNER_HTTPS') == '1',
    )
    if test_config:
        app.config.update(test_config)

    def db():
        if 'db' not in g:
            g.db = sqlite3.connect(app.config['DATABASE'])
            g.db.row_factory = sqlite3.Row
            g.db.execute('PRAGMA foreign_keys=ON')
        return g.db

    @app.teardown_appcontext
    def close_db(error=None):
        conn = g.pop('db', None)
        if conn is not None:
            conn.close()

    with app.app_context():
        db().executescript((Path(__file__).parent / 'schema.sql').read_text())

    @app.cli.command('create-user')
    @click.argument('email')
    @click.password_option(confirmation_prompt=True)
    def create_user(email, password):
        """Cria um consultor local com senha digitada sem eco."""
        if len(password) < 12:
            raise click.ClickException('Use pelo menos 12 caracteres.')
        try:
            db().execute('INSERT INTO users(email,password_hash) VALUES (?,?)',
                         (email.strip().lower(), generate_password_hash(password)))
            db().commit()
        except sqlite3.IntegrityError:
            raise click.ClickException('Usuário já cadastrado.') from None
        click.echo('Consultor criado.')

    def login_required(view):
        @functools.wraps(view)
        def wrapped(**kwargs):
            if g.user is None:
                return redirect(url_for('login'))
            return view(**kwargs)
        return wrapped

    def csrf_token():
        if 'csrf' not in session:
            session['csrf'] = secrets.token_hex(24)
        return session['csrf']
    app.jinja_env.globals['csrf_token'] = csrf_token

    @app.before_request
    def authenticate():
        g.user = db().execute('SELECT id,email FROM users WHERE id=?',
                              (session.get('user_id'),)).fetchone()
        if request.method == 'POST':
            expected = session.get('csrf', '')
            provided = request.form.get('csrf', '')
            if not expected or not secrets.compare_digest(expected, provided):
                abort(400, 'Sessão expirada. Recarregue a página e tente novamente.')

    @app.after_request
    def headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'"
        response.headers['Cache-Control'] = 'no-store'
        return response

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = db().execute('SELECT * FROM users WHERE email=?',
                                (request.form.get('email', '').strip().lower(),)).fetchone()
            if user and check_password_hash(user['password_hash'], request.form.get('password', '')):
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('dashboard'))
            flash('E-mail ou senha incorretos.', 'error')
        return render_template('login.html', title='Entrar')

    @app.post('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))

    @app.get('/')
    @login_required
    def dashboard():
        clients = db().execute('SELECT COUNT(*) FROM clients WHERE owner_id=?', (g.user['id'],)).fetchone()[0]
        runs = db().execute('''SELECT a.*,c.name client_name FROM analyses a JOIN clients c
            ON c.id=a.client_id WHERE c.owner_id=? ORDER BY a.id DESC''', (g.user['id'],)).fetchall()
        return render_template('dashboard.html', title='Visão geral', clients=clients, runs=runs)

    @app.route('/clientes', methods=['GET', 'POST'])
    @login_required
    def clients():
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            environment = request.form.get('environment', '').strip()
            if not 2 <= len(name) <= 100 or not 2 <= len(environment) <= 100:
                flash('Informe cliente e ambiente com 2 a 100 caracteres.', 'error')
            else:
                db().execute('INSERT INTO clients(owner_id,name,environment) VALUES (?,?,?)',
                             (g.user['id'], name, environment))
                db().commit()
                flash('Cliente cadastrado.', 'success')
                return redirect(url_for('clients'))
        rows = db().execute('SELECT * FROM clients WHERE owner_id=? ORDER BY name', (g.user['id'],)).fetchall()
        return render_template('clients.html', title='Clientes e ambientes', clients=rows)

    @app.route('/analises/nova', methods=['GET', 'POST'])
    @login_required
    def new_analysis():
        clients = db().execute('SELECT * FROM clients WHERE owner_id=? ORDER BY name', (g.user['id'],)).fetchall()
        if request.method == 'POST':
            client = db().execute('SELECT * FROM clients WHERE id=? AND owner_id=?',
                                 (request.form.get('client_id'), g.user['id'])).fetchone()
            if client is None:
                abort(404)
            upload = request.files.get('config_file')
            try:
                if request.form.get('authorized') != 'yes':
                    raise ValueError('Confirme que o arquivo é sintético ou autorizado e anonimizado.')
                if not upload or not upload.filename.lower().endswith(('.txt', '.cfg')):
                    raise ValueError('Selecione um arquivo .txt ou .cfg.')
                raw = upload.stream.read(256 * 1024 + 1)
                if len(raw) > 256 * 1024:
                    raise ValueError('O arquivo deve ter no máximo 256 KB.')
                text = raw.decode('utf-8')
                validate_config(text)
                inventory, findings = analyze(text)
            except (ValueError, UnicodeDecodeError) as error:
                message = 'Use um arquivo de texto UTF-8.' if isinstance(error, UnicodeDecodeError) else str(error)
                flash(message, 'error')
            else:
                with db():
                    cursor = db().execute('INSERT INTO analyses(client_id,hostname,inventory) VALUES (?,?,?)',
                                          (client['id'], inventory['hostname'], json.dumps(inventory)))
                    analysis_id = cursor.lastrowid
                    for item in findings:
                        db().execute('''INSERT INTO findings(analysis_id,rule_id,title,severity,evidence,recommendation)
                            VALUES (?,?,?,?,?,?)''', (analysis_id, item['id'], item['title'], item['severity'], item['evidence'], item['recommendation']))
                    db().execute('INSERT INTO events(analysis_id,actor_id,action) VALUES (?,?,?)',
                                 (analysis_id, g.user['id'], 'Análise criada; regras v1; arquivo bruto descartado'))
                return redirect(url_for('analysis', analysis_id=analysis_id))
        return render_template('upload.html', title='Nova análise', clients=clients)

    def get_analysis(analysis_id):
        row = db().execute('''SELECT a.*,c.name client_name,c.environment FROM analyses a JOIN clients c
            ON c.id=a.client_id WHERE a.id=? AND c.owner_id=?''', (analysis_id, g.user['id'])).fetchone()
        if row is None:
            abort(404)
        return row

    @app.get('/analises/<int:analysis_id>')
    @login_required
    def analysis(analysis_id):
        row = get_analysis(analysis_id)
        findings = db().execute('SELECT * FROM findings WHERE analysis_id=? ORDER BY id', (analysis_id,)).fetchall()
        events = db().execute('''SELECT e.*,u.email FROM events e JOIN users u ON u.id=e.actor_id
            WHERE analysis_id=? ORDER BY e.id DESC''', (analysis_id,)).fetchall()
        return render_template('analysis.html', title='Revisão técnica', analysis=row,
                               inventory=json.loads(row['inventory']), findings=findings, events=events,
                               pending=sum(f['decision'] == 'Pendente' for f in findings))

    @app.post('/analises/<int:analysis_id>/achados/<int:finding_id>')
    @login_required
    def review(analysis_id, finding_id):
        get_analysis(analysis_id)
        finding = db().execute('SELECT id FROM findings WHERE id=? AND analysis_id=?', (finding_id, analysis_id)).fetchone()
        if finding is None:
            abort(404)
        decision = request.form.get('decision')
        note = request.form.get('note', '').strip()
        if decision not in ('Confirmado', 'Descartado') or not 5 <= len(note) <= 1000:
            flash('Escolha uma decisão e justifique com 5 a 1.000 caracteres.', 'error')
            return redirect(url_for('analysis', analysis_id=analysis_id))
        with db():
            db().execute('UPDATE findings SET decision=?,note=? WHERE id=?', (decision, note, finding_id))
            db().execute("UPDATE analyses SET status='Em revisão' WHERE id=?", (analysis_id,))
            db().execute('INSERT INTO events(analysis_id,actor_id,action) VALUES (?,?,?)',
                         (analysis_id, g.user['id'], f'Achado {finding_id}: {decision}. {note}'))
        flash('Revisão salva. Alterações exigem nova liberação do relatório.', 'success')
        return redirect(url_for('analysis', analysis_id=analysis_id))

    @app.post('/analises/<int:analysis_id>/liberar')
    @login_required
    def release(analysis_id):
        get_analysis(analysis_id)
        pending = db().execute("SELECT COUNT(*) FROM findings WHERE analysis_id=? AND decision='Pendente'", (analysis_id,)).fetchone()[0]
        if pending or request.form.get('reviewed') != 'yes':
            flash('Revise todos os achados e confirme a revisão final.', 'error')
            return redirect(url_for('analysis', analysis_id=analysis_id))
        with db():
            db().execute("UPDATE analyses SET status='Liberado' WHERE id=?", (analysis_id,))
            db().execute('INSERT INTO events(analysis_id,actor_id,action) VALUES (?,?,?)',
                         (analysis_id, g.user['id'], 'Relatório liberado após revisão final'))
        return redirect(url_for('report', analysis_id=analysis_id))

    @app.get('/analises/<int:analysis_id>/relatorio')
    @login_required
    def report(analysis_id):
        row = get_analysis(analysis_id)
        if row['status'] != 'Liberado':
            abort(403, 'Relatório ainda não liberado pelo consultor.')
        findings = db().execute('SELECT * FROM findings WHERE analysis_id=?', (analysis_id,)).fetchall()
        return render_template('report.html', title='Relatório técnico', analysis=row, findings=findings)

    @app.post('/analises/<int:analysis_id>/excluir')
    @login_required
    def delete_analysis(analysis_id):
        get_analysis(analysis_id)
        if request.form.get('confirmation') != 'EXCLUIR':
            flash('Digite EXCLUIR para confirmar.', 'error')
            return redirect(url_for('analysis', analysis_id=analysis_id))
        with db():
            db().execute('DELETE FROM analyses WHERE id=?', (analysis_id,))
        flash('Análise, achados e histórico excluídos da base ativa.', 'success')
        return redirect(url_for('dashboard'))

    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(413)
    def error_page(error):
        messages = {400: 'Requisição inválida. Recarregue a página.', 403: 'Acesso indisponível para este relatório.',
                    404: 'Registro não encontrado.', 413: 'Arquivo ou requisição excede o limite permitido.'}
        return render_template('error.html', title=str(error.code), message=messages[error.code]), error.code

    return app
