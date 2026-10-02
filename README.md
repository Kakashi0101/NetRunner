# Netrunner OT

A **Netrunner OT** é uma proposta de plataforma web para diagnóstico e melhoria contínua de redes industriais. Combina análise de configurações, regras determinísticas, triagem por inteligência artificial e revisão humana especializada.

> Projeto acadêmico em fase de documentação. O aplicativo ainda não está implementado. Atualização: 01/10/2026.

## Objetivo

Auxiliar equipes de TI/OT e integradores a identificar riscos e organizar recomendações de melhoria em configurações de rede, com evidências, prioridades, testes e plano de retorno.

## Documentação e entregas

- [Documento de Contexto](Documento%20de%20Contexto.md)
- [Especificação do Projeto](Especifica%C3%A7%C3%A3o%20do%20Projeto.md)
- [Plano de Negócios](Plano%20de%20Neg%C3%B3cios.md)
- Lean Canvas, missão, visão e valores: incluídos no Documento de Contexto.
- [Lean Canvas ilustrado original](lean_canvas_netrunner_ot.png), como referência da concepção inicial. Para escopo e modelo comercial atualizados, consultar os documentos em Markdown.
- [Memória de cálculo dos cenários](scripts/calcular_cenarios.py)

O Plano de Negócios apresenta cenários Lean e ideal, investimentos, capital de giro, custos e despesas, enquadramento tributário proposto, precificação, resultado mensal, equilíbrio, CAC, ARPU e LTV. Valores financeiros são hipóteses acadêmicas, não cotações ou resultados de operação. As referências aos materiais de aula estão no próprio plano.

## Escopo inicial do MVP

1. Cadastro do cliente e do ambiente.
2. Upload manual de configuração anonimizada.
3. Extração de informações e aplicação de regras técnicas.
4. Triagem preliminar por IA.
5. Revisão dos achados pelo consultor.
6. Liberação do relatório com recomendações e prioridades.
7. Planejamento assistido de correções, validação e rollback, mediante contratação.

O MVP não aplicará comandos nos equipamentos, não fará monitoramento em tempo real e não terá integração automática de cobrança. Franquias e horas serão controladas manualmente no piloto.

## Arquivos do repositório

| Arquivo | Finalidade |
|---|---|
| `README.md` | Apresentação e acesso às entregas |
| `Documento de Contexto.md` | Problema, público, solução e modelo de negócio |
| `Especificação do Projeto.md` | Escopo, requisitos, arquitetura e critérios de aceite |
| `Plano de Negócios.md` | Cenários financeiros, tributos e precificação |
| `lean_canvas_netrunner_ot.png` | Ilustração original do Lean Canvas |
| `scripts/calcular_cenarios.py` | Reprodução das contas em Python 3 |

## Reprodução dos cálculos

Não é necessário instalar dependências externas:

```bash
python scripts/calcular_cenarios.py
```

O script simula cenários estabilizados na referência tributária de 2026. Não substitui apuração contábil e não implementa o aplicativo Netrunner OT.

## Conferência e envio ao Canvas

1. Conferir os três documentos e os links acima na versão publicada do repositório.
2. No GitHub, acessar **Code → Download ZIP** após a atualização.
3. Enviar o ZIP completo à atividade correspondente no Canvas, conforme o enunciado.

Não enviar apenas o Plano de Negócios: a entrega exige o download completo do repositório atualizado.

## Segurança

Não publique configurações reais com senhas, chaves, comunidades SNMP ou informações sensíveis de clientes. Utilize dados sintéticos ou explicitamente autorizados e anonimizados. Nenhuma recomendação será implantada sem análise de impacto, aprovação, backup e plano de retorno.
