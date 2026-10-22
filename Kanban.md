# Kanban — Etapa 3

Atualizado em 21/10/2026. Quadro versionado em Markdown e vinculado a issues reais. Este arquivo não é um GitHub Project nativo; o grupo pode criar a visualização Board em Projects e adicionar as mesmas issues.

| A fazer | Em andamento | Em revisão | Concluído nesta implementação |
|---|---|---|---|
| [#2 Busca e edição de clientes](https://github.com/Kakashi0101/NetRunner/issues/2) | Nenhuma tarefa individual assumida no momento deste registro | [#1 Validação do grupo e demonstração](https://github.com/Kakashi0101/NetRunner/issues/1) | Telas de login, dashboard, clientes, upload, revisão e relatório |
| [#3 Catálogo de 20 regras](https://github.com/Kakashi0101/NetRunner/issues/3) | | | Backend, banco e seis regras |
| [#4 Acessibilidade e contribuições](https://github.com/Kakashi0101/NetRunner/issues/4) | | | Testes automatizados iniciais |
| [#5 Segurança para piloto](https://github.com/Kakashi0101/NetRunner/issues/5) | | | Documentação de interface, template, arquitetura e SWOT |
| [#6 Validação financeira e BSC](https://github.com/Kakashi0101/NetRunner/issues/6) | | | Planilhas com fórmulas e hipóteses editáveis |

## Política de trabalho

- **A fazer:** issue com escopo e aceite definidos, ainda sem implementação iniciada.
- **Em andamento:** integrante identificado, branch criada e trabalho real iniciado. Limite proposto de uma tarefa por integrante.
- **Em revisão:** PR aberto, testes executados e evidências anexadas; revisão pendente.
- **Concluído:** aceite verificado, revisão registrada e alteração integrada. Conclusão técnica assistida por IA não comprova participação de toda a equipe.

Ao assumir uma tarefa, o integrante deve atribuir a issue à sua conta e mover o cartão no quadro. Nenhum responsável foi inventado ou atribuído sem confirmação. As issues da próxima rodada têm critérios de aceite e nomes de branch sugeridos.

## Branches

Fluxo proposto: `feature/<tema>` nasce de `develop`; PR integra em `develop`; uma entrega validada segue por PR para `main`. `main` mantém a versão de entrega, e `develop` mantém a integração. Correções urgentes podem usar `hotfix/<tema>` e retornar a ambas. Não fazer force push no histórico compartilhado.

Nesta Etapa 3, o pacote inicial é desenvolvido em `feature/etapa3`. O grupo continuará a partir de issues próprias, sem dividir artificialmente um único trabalho em autores fictícios.
