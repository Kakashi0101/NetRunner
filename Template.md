# Template — Netrunner OT

Etapa 3 · 21/10/2026.

## 1. Interpretação adotada

Como o enunciado solicita `Template.md` junto do projeto de interface, este documento descreve o template visual implementado e a estrutura para novas telas. Caso exista um modelo institucional adicional, o grupo deverá compatibilizá-lo com esta documentação.

## 2. Identidade visual

| Elemento | Definição | Uso |
|---|---|---|
| Azul escuro | `#11263B` | Navegação e identidade |
| Texto principal | `#172E43` | Títulos e corpo |
| Verde de ação | `#087F78` | Botões e links |
| Fundo | `#F4F7FA` | Área de trabalho |
| Superfície | `#FFFFFF` | Formulários e tabelas |
| Erro | `#AC3131` | Avisos e ação de exclusão |
| Tipografia | Arial, Helvetica, sans-serif | Fontes locais, sem CDN |

O nome Netrunner OT e a marca tipográfica são montados em HTML/CSS. Não há dependência de bibliotecas de componentes ou imagens remotas.

## 3. Template base implementado

O arquivo [base.html](app/templates/base.html) contém título da página, navegação, sessão do usuário, mensagens e rodapé. Cada tela estende esse template e preenche os blocos `action` e `content`.

```html
{% extends 'base.html' %}
{% block action %}
<a class="button" href="{{ url_for('new_analysis') }}">Nova análise</a>
{% endblock %}
{% block content %}
<section class="panel">
  <h2>Conteúdo da tela</h2>
  <p>Dados reais fornecidos pela rota Flask.</p>
</section>
{% endblock %}
```

## 4. Componentes reutilizáveis

| Componente CSS | Responsabilidade | Exemplo |
|---|---|---|
| `.page-heading` | Título e ação principal | Nova análise |
| `.panel` | Seção de conteúdo ou formulário | Cadastro de cliente |
| `.metrics` | Indicadores consultados no banco | Dashboard e revisão |
| `.notice` | Mensagem informativa ou erro | Upload rejeitado |
| `.badge` | Status com texto explícito | Alta / A confirmar |
| `.table-wrap` | Tabela com rolagem localizada | Histórico |
| `.checkbox` | Confirmação explícita | Autorização e liberação |
| `.finding` | Evidência e formulário de revisão | Achado técnico |

## 5. Padrão de formulários

Cada `POST` inclui token CSRF, campos com label e validação no servidor. Valores não confiáveis passam pelo escape padrão do Jinja. Senhas são enviadas somente para validação e não voltam ao HTML. O desenvolvimento local usa HTTP em loopback; implantação externa exige HTTPS.

Novas telas devem preservar: navegação por teclado, foco visível, estado vazio útil, mensagem de erro compreensível, limites de entrada e isolamento por proprietário. O CSS de impressão remove navegação no relatório.

## 6. Estrutura de código

```text
app/
  __init__.py       Rotas, sessão e operações de persistência
  analyzer.py       Parser e regras determinísticas
  schema.sql        Estrutura SQLite
  templates/       Base e telas Jinja
  static/app.css   Estilos compartilhados
tests/test_app.py   Testes de regras e fluxos HTTP
```

O template já é utilizado por todas as telas da aplicação. Mudanças em componentes compartilhados precisam ser verificadas nas telas de login, cadastro, revisão e relatório.
