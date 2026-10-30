# Kanban — Etapa 3

Atualizado em 29/10/2026. Quadro versionado em Markdown e vinculado às issues do repositório. Não há um quadro nativo do GitHub Projects registrado nesta documentação.

| A fazer | Em andamento | Em revisão | Concluído nesta implementação |
|---|---|---|---|
| [#2 Busca e edição de clientes](https://github.com/Kakashi0101/NetRunner/issues/2) | Sem tarefa atribuída | Sem PR aberto | Telas de login, dashboard, clientes, upload, revisão e relatório |
| [#3 Catálogo de 20 regras](https://github.com/Kakashi0101/NetRunner/issues/3) | | | Backend, banco e seis regras |
| [#4 Acessibilidade e contribuições](https://github.com/Kakashi0101/NetRunner/issues/4) | | | Testes automatizados iniciais |
| [#5 Segurança para piloto](https://github.com/Kakashi0101/NetRunner/issues/5) | | | Documentação de interface, template, arquitetura e SWOT |
| [#6 Validação financeira e BSC](https://github.com/Kakashi0101/NetRunner/issues/6) | | | Planilhas com fórmulas e hipóteses editáveis |
| [#1 Validação do grupo e demonstração](https://github.com/Kakashi0101/NetRunner/issues/1) | | | |

## Política de trabalho

- **A fazer:** issue com escopo e aceite definidos, ainda sem implementação iniciada.
- **Em andamento:** integrante identificado, branch criada e trabalho real iniciado. Limite proposto de uma tarefa por integrante.
- **Em revisão:** PR aberto, testes executados e evidências anexadas; revisão pendente.
- **Concluído:** aceite verificado, revisão registrada e alteração integrada. Conclusão técnica assistida por IA não comprova participação de toda a equipe.

As seis issues abertas estão sem responsáveis atribuídos no GitHub. Cada issue contém escopo, critérios de aceite e uma proposta de branch.

## Branches

Fluxo proposto: `feature/<tema>` nasce de `develop`; PR integra em `develop`; uma entrega validada segue por PR para `main`. `main` mantém a versão de entrega, e `develop` mantém a integração. Correções urgentes podem usar `hotfix/<tema>` e retornar a ambas. Não fazer force push no histórico compartilhado.

O pacote inicial foi integrado de `feature/etapa3` para `develop` pelo [PR #7](https://github.com/Kakashi0101/NetRunner/pull/7) e de `develop` para `main` pelo [PR #8](https://github.com/Kakashi0101/NetRunner/pull/8).
