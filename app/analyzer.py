"""Regras v1: achados preliminares, sem conexão a dispositivos ou IA externa."""
import re

SENSITIVE = re.compile(r'^\s*(?:username\s|enable\s+(?:secret|password)\b|(?:password|secret)\s|snmp-server\s+community\b|.*\b(?:key-string|private-key|pre-shared-key)\b|crypto\s+pki\s+certificate\b)', re.I | re.M)


def validate_config(text):
    if not text.strip() or '\x00' in text:
        raise ValueError('Arquivo vazio ou conteúdo binário não suportado.')
    if SENSITIVE.search(text):
        raise ValueError('Possível segredo detectado. Remova linhas com credenciais ou chaves antes do envio.')
    if not re.search(r'^hostname\s+[\w.-]{1,100}\s*$', text, re.M) or not re.search(r'^interface\s+\S+', text, re.M):
        raise ValueError('Formato não reconhecido. Envie configuração IOS/IOS-XE com hostname e interface.')


def analyze(text):
    validate_config(text)
    lines = text.splitlines()
    inventory = {
        'hostname': re.search(r'^hostname\s+([\w.-]+)', text, re.M).group(1),
        'interfaces': re.findall(r'^interface\s+(\S+)', text, re.M),
        'vlans': re.findall(r'^vlan\s+(\d+)', text, re.M),
        'version': next((s[8:] for s in lines if s.startswith('version ')), 'Não informada'),
    }
    findings = []

    def add(rule_id, title, severity, evidence, recommendation):
        findings.append(dict(id=rule_id, title=title, severity=severity,
                             evidence=evidence[:500], recommendation=recommendation))

    for number, line in enumerate(lines, 1):
        clean = line.strip()
        if re.fullmatch(r'transport input (?:.*\btelnet\b.*|all)', clean):
            add('NET-001', 'Acesso Telnet permitido', 'Alta', f'Linha {number}: {clean}',
                'Validar SSH e acesso alternativo antes de restringir o transporte em janela aprovada.')
        if clean == 'ip http server':
            add('NET-002', 'Gerenciamento HTTP habilitado', 'Alta', f'Linha {number}: {clean}',
                'Confirmar dependências de gerenciamento e avaliar HTTPS antes de desabilitar HTTP.')
        if clean == 'switchport trunk allowed vlan all':
            add('NET-003', 'Trunk permite todas as VLANs', 'Média', f'Linha {number}: {clean}',
                'Relacionar VLANs necessárias e validar conectividade antes de restringir a lista.')
    for rule_id, title, pattern, recommendation in [
        ('NET-004', 'NTP não evidenciado no arquivo', r'^ntp (?:server|peer)\s', 'Confirmar sincronismo e origem de tempo autorizada no ambiente.'),
        ('NET-005', 'Syslog remoto não evidenciado', r'^logging (?:host\s+)?(?:\d|[a-zA-Z])', 'Confirmar coletor remoto e política de retenção de logs.'),
        ('NET-006', 'SSH versão 2 não explicitado', r'^ip ssh version 2\s*$', 'Verificar versão e padrões da plataforma antes de recomendar configuração.'),
    ]:
        # Exclui diretivas locais de logging que não representam um destino remoto.
        inspected = '\n'.join(s for s in lines if not re.match(r'^logging (?:buffered|console|monitor|trap|source-interface|on|facility|origin-id)\b', s))
        if not re.search(pattern, inspected, re.M):
            add(rule_id, title, 'A confirmar', 'Comando esperado não localizado no arquivo fornecido; arquivo pode estar incompleto.', recommendation)
    return inventory, findings
