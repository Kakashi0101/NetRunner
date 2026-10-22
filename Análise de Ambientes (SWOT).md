# Análise de Ambientes (SWOT) — Netrunner OT

Etapa 3 · 21/10/2026. Avaliação qualitativa derivada do escopo técnico e das hipóteses do Plano de Negócios. Oportunidades e ameaças são hipóteses a validar em entrevistas, não pesquisa de mercado concluída.

## 1. Matriz

| Forças — ambiente interno | Fraquezas — ambiente interno |
|---|---|
| F1. Escopo voltado à análise de configurações de redes industriais. | W1. Parser inicial parcial e catálogo de somente seis regras. |
| F2. Evidência rastreável, revisão humana e registro das decisões já implementados. | W2. Dependência de horas de consultoria e de conhecimento especializado. |
| F3. Fluxo local com dados sintéticos, sem acesso direto aos equipamentos. | W3. Ausência de pilotos comerciais e de disposição a pagar comprovada. |
| F4. Custos, preços e carteira documentados com premissas editáveis. | W4. Controles para operação externa, papéis e participação de todos os integrantes ainda pendentes. |

| Oportunidades — ambiente externo | Ameaças — ambiente externo |
|---|---|
| O1. Empresas com equipes reduzidas podem precisar de revisão periódica. | T1. Clientes podem preferir consultorias e ferramentas já contratadas. |
| O2. Integradores podem utilizar o serviço em sua carteira. | T2. Configurações incompletas e diferenças de plataforma podem levar a recomendações inadequadas. |
| O3. Auditorias e modernizações podem gerar demanda por documentação. | T3. Incidentes de confidencialidade podem inviabilizar confiança comercial. |
| O4. Acompanhamento recorrente pode gerar receita após um diagnóstico avulso. | T4. Variação de custos, tributos e ciclo comercial pode consumir a reserva de caixa. |

## 2. Estratégias cruzadas

| Combinação | Ação | Indicador BSC | Evidência esperada |
|---|---|---|---|
| F1 + O2 | Entrevistar integradores e demonstrar diagnóstico com arquivo sintético. | F1, C1 | Registro de entrevista e proposta de piloto |
| F2 + O3 | Demonstrar origem de cada evidência e a revisão antes da entrega. | P2, C3 | Relatório revisado e histórico |
| W1 + O1 | Ampliar regras mais frequentes nos pilotos antes de aumentar fabricantes. | P1 | Regras testadas e PRs individuais |
| W3 + O4 | Validar valor e preço com piloto pago antes de ampliar custos fixos. | F1, F2, C2 | Conversão, CAC e cancelamentos medidos |
| F2 + T2 | Exigir validação de contexto e justificar falsos positivos. | P2, P3 | Decisões técnicas e tempo de revisão |
| F4 + T4 | Atualizar fluxo com recebimentos, perdas e custos reais todo mês. | F3 | Reserva disponível e compromissos futuros |
| W4 + T3 | Resolver controles pendentes antes de receber dados reais externamente. | P2, A1 | Testes de acesso, backup e retenção |
| W2 + T1 | Capacitar mais revisores e medir produtividade sem reduzir qualidade. | A1, A3, P3 | Revisões por pares e horas por diagnóstico |

## 3. Prioridades e acompanhamento

Prioridade imediata: completar participação individual e validar a execução do MVP. Prioridade técnica seguinte: regras, qualidade e segurança. Prioridade comercial: entrevistas e custos medidos, antes de assumir a carteira do cenário ideal.

As ações estão no [Kanban](Kanban.md), com critérios de aceite nas issues. Revisão proposta da SWOT: ao fim de cada piloto ou quando uma hipótese comercial/tecnológica mudar. Responsáveis individuais serão definidos pelo grupo; os papéis propostos constam no [Balanced Scorecard](planilhas/Balanced_Scorecard.xlsx).
