# Registro de validação — Etapa 3

Data: 21/10/2026. Ambiente de teste: Python 3.12 em Linux, Flask 3.1.2 e pytest 8.4.2.

## Verificações executadas

- `python -m pytest -q`: **16 testes aprovados**, incluindo os casos parametrizados.
- Fluxo HTTP completo: autenticação, cliente, upload sintético, seis achados, revisão, liberação, revogação após alteração e exclusão.
- Isolamento: segunda conta não acessa análise, relatório, revisão, upload para cliente alheio ou exclusão de outra conta.
- Proteções testadas: token CSRF, escape de HTML, padrões de segredo, limite de arquivo e validação de formato.
- Persistência: registros continuam disponíveis após recriar a aplicação com a mesma base.
- Planilhas: recálculo, fórmulas sem erros na varredura, troca de cenário e prazo de recebimento, conferência independente do saldo final e inspeção visual de todas as abas.

## Limitações da validação

Os testes HTTP renderizam os templates, mas não substituem teste visual/interativo em um navegador. A tentativa de instalar o navegador de automação não produziu um executável utilizável neste ambiente. Portanto, não se declara validação visual de desktop/mobile nem acessibilidade com leitor de tela. Essas verificações são acompanhadas na [issue 1](https://github.com/Kakashi0101/NetRunner/issues/1) e na [issue 4](https://github.com/Kakashi0101/NetRunner/issues/4).

Não foram executados testes em equipamentos industriais, dados reais, carga, concorrência elevada, Windows ou Microsoft Excel. O README contém as instruções de execução local no Windows.

## Roteiro de demonstração manual

1. Criar ambiente virtual, instalar dependências e cadastrar consultor com `flask create-user`.
2. Abrir a aplicação, entrar e conferir o estado vazio do dashboard.
3. Cadastrar cliente “Indústria Demonstração” e ambiente “Laboratório”.
4. Enviar `examples/switch_sintetico.cfg`, confirmando a autorização.
5. Conferir as seis regras e tentar abrir o relatório antes da liberação: deve ser bloqueado.
6. Confirmar ou descartar cada achado com justificativa e liberar o relatório.
7. Voltar à revisão e alterar uma decisão: o relatório deve exigir nova liberação.
8. Repetir com outra conta para conferir o isolamento.
9. Reduzir a largura da janela e navegar por teclado. Registrar as capturas em `docs/evidencias/`.
10. Abrir as planilhas no Excel, alterar o cenário e um resultado do BSC, conferindo recálculo.

Os dados de demonstração são sintéticos; senhas, bases locais e configurações reais não fazem parte das evidências públicas.
