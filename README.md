# Netrunner OT

Diagnóstico de configurações de redes industriais com regras rastreáveis e revisão humana. **Etapa 3: implementação inicial funcional, local, em Python/Flask e SQLite.**

O consultor pode entrar, cadastrar cliente/ambiente, enviar uma configuração sintética, executar seis regras, revisar achados e liberar um relatório. Os dados permanecem no banco após reiniciar a aplicação. IA externa, portal do cliente, comparação de versões e o catálogo completo de 20 regras ainda não foram implementados.

## Entregas da Etapa 3

| Item | Documento ou evidência |
|---|---|
| Projeto de interface | [Projeto de Interface.md](Projeto%20de%20Interface.md) |
| Template implementado | [Template.md](Template.md) |
| Arquitetura e stack | [Arquitetura do Sistema.md](Arquitetura%20do%20Sistema.md) |
| Balanced Scorecard | [Planilha com 12 objetivos, três por perspectiva](planilhas/Balanced_Scorecard.xlsx) |
| Análise de ambientes | [SWOT](An%C3%A1lise%20de%20Ambientes%20%28SWOT%29.md) |
| Fluxo de caixa | [Planilha Lean/Ideal com fórmulas](planilhas/Fluxo_de_Caixa.xlsx) e [premissas](planilhas/README.md) |
| Contribuições individuais | [Registro de contribuições](Contribui%C3%A7%C3%B5es%20Individuais.md) |
| Organização das tarefas | [Kanban versionado](Kanban.md) e [issues](https://github.com/Kakashi0101/NetRunner/issues) |
| Implementação | [Código](app), [testes](tests/test_app.py) e [validação](docs/VALIDACAO.md) |

A autoria e as evidências de participação estão no [registro de contribuições](Contribui%C3%A7%C3%B5es%20Individuais.md).

## Entregas anteriores

- [Documento de Contexto](Documento%20de%20Contexto.md)
- [Especificação do Projeto](Especifica%C3%A7%C3%A3o%20do%20Projeto.md)
- [Plano de Negócios](Plano%20de%20Neg%C3%B3cios.md)
- Lean Canvas, missão, visão e valores no Documento de Contexto.
- [Lean Canvas ilustrado original](lean_canvas_netrunner_ot.png), preservado como referência da concepção inicial.
- [Memória de cálculo anterior](scripts/calcular_cenarios.py).

## Executar no Windows com Git Bash

Pré-requisitos: Python 3.12 instalado e Git. Na pasta deste repositório:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python -m flask --app app create-user seu-email@example.com
python -m flask --app app run --host 127.0.0.1 --port 5000
```

Use seu e-mail no comando de criação. A senha será solicitada sem eco e precisa ter pelo menos 12 caracteres. Não existe senha padrão. Se `python` não for reconhecido, tente `py -3.12` para criar o ambiente.

Abra **http://127.0.0.1:5000**. No Linux/macOS, a ativação do ambiente é `source .venv/bin/activate`; os demais comandos são iguais.

## Demonstrar a funcionalidade

1. Entre com o usuário criado.
2. Em **Clientes e ambientes**, cadastre um cliente de demonstração.
3. Em **Nova análise**, envie [switch_sintetico.cfg](examples/switch_sintetico.cfg) e confirme a autorização.
4. O backend cria seis achados. Confirme ou descarte cada um com justificativa.
5. Confirme a revisão final e clique em **Liberar relatório**.
6. Use a impressão do navegador para salvar em PDF, se necessário.

Uma nova edição em um achado retorna a análise para revisão e bloqueia o relatório até nova liberação. A exclusão exige digitar EXCLUIR. O arquivo bruto não é armazenado; o inventário e as evidências ficam no SQLite.

## Testes

Com o ambiente virtual ativado:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Resultado da validação inicial: **16 testes aprovados**. A suíte cobre regras, persistência, autenticação, CSRF, isolamento e revisão/liberação. Há workflow em [.github/workflows/tests.yml](.github/workflows/tests.yml). A execução da versão inicial na `main` também foi [aprovada no GitHub Actions](https://github.com/Kakashi0101/NetRunner/actions/runs/39699944030).

A validação visual em navegador, no Windows e com leitores de tela ainda não possui evidências registradas. O escopo dos testes está em [VALIDACAO.md](docs/VALIDACAO.md).

## Organização

| Local | Conteúdo |
|---|---|
| `app/` | Backend, regras, esquema, templates e CSS |
| `tests/` | Testes automatizados |
| `examples/` | Configuração sintética para demonstração |
| `planilhas/` | Balanced Scorecard, fluxo de caixa e instruções |
| `docs/` | Validação e referências de evidências |
| `instance/` | Banco e chave locais, gerados e ignorados pelo Git |

Use `feature/<tema>` para trabalho individual, PR para `develop` e PR de entrega para `main`. A política de revisão está no [Kanban](Kanban.md).

## Limites desta versão

A aplicação é uma base acadêmica local. Não possui rate limiting, papéis completos, criptografia de aplicação no banco, retenção automática ou backup gerenciado. O parser é parcial e não certifica a saúde da rede. Use dados sintéticos até concluir os controles da [issue de segurança](https://github.com/Kakashi0101/NetRunner/issues/5). Não exponha o servidor de desenvolvimento diretamente à internet.

