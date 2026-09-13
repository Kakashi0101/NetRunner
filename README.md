# Netrunner OT

A **Netrunner OT** é uma proposta de plataforma web para diagnóstico, conformidade e melhoria contínua de redes industriais. A solução combina análise automatizada, um agente de inteligência artificial para triagem preliminar e revisão humana especializada.

> Este repositório contém os artefatos da Etapa 1 do projeto acadêmico.

## Objetivo

Auxiliar organizações a identificar riscos técnicos e oportunidades de melhoria em configurações de switches, roteadores e outros ativos de rede, entregando relatórios priorizados e apoio consultivo para correção.

## Entregas da Etapa 1

- [Documento de Contexto](docs/Documento%20de%20Contexto.md)
- [Especificação do Projeto](docs/Especificação%20do%20Projeto.md)
- Lean Canvas, incluído no Documento de Contexto
- Missão, Visão e Valores, incluídos no Documento de Contexto

## Escopo inicial do MVP

1. Cadastro do cliente e do ambiente analisado.
2. Upload manual de uma `running-config` anonimizada.
3. Extração das principais informações da configuração.
4. Aplicação de regras técnicas determinísticas.
5. Triagem preliminar por agente de IA.
6. Revisão dos achados pelo consultor.
7. Emissão de relatório com riscos, recomendações e prioridades.
8. Geração assistida de correções, validações e rollback.

## Estrutura do repositório

```text
netrunner-ot/
├── README.md
├── .gitignore
├── LICENSE
├── docs/
│   ├── Documento de Contexto.md
│   └── Especificação do Projeto.md
├── config/
│   └── exemplo_anonimizado.txt
└── src/
    └── README.md
```

## Status

Etapa 1: definição do contexto, especificação inicial, Lean Canvas e identidade organizacional.

## Segurança

Não envie configurações reais contendo senhas, chaves, comunidades SNMP, endereços sensíveis ou informações de clientes. Todo arquivo utilizado em testes deverá passar por anonimização.
