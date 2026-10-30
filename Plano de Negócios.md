# Plano de Negócios: Netrunner OT

**Disciplina:** Trabalho Acadêmico Integrado III • **Data-base:** 01/10/2026

## 1. Resumo executivo

A Netrunner OT propõe uma plataforma web de diagnóstico de configurações de redes industriais, associada à consultoria especializada. O cliente envia arquivos anonimizados, o sistema extrai informações e executa regras técnicas, a IA auxilia na triagem e um consultor revisa os resultados antes da entrega. A proposta atende pequenas e médias indústrias e integradores que precisam documentar e melhorar redes, mas dispõem de equipes reduzidas.

O modelo comercial combina assinatura mensal com franquia de equipamentos e revisão humana, diagnóstico avulso e contratação separada de remediação. Não inclui monitoramento contínuo nem execução automática de comandos.

O cenário **Lean** utiliza operação remota, desenvolvimento contratado em pequena escala e revisão técnica sob demanda. O cenário **ideal** amplia desenvolvimento, segurança, capacidade comercial e rede de consultores. A recomendação é iniciar pelo Lean e ampliar a estrutura somente após comprovar demanda, retenção e capacidade de entrega.

> Todos os preços, volumes, horas, taxas comerciais e orçamentos deste plano são **estimativas acadêmicas propostas**, não cotações, contratos ou resultados observados. Na data-base deste plano, o repositório continha documentação; na Etapa 3 foi adicionada uma implementação inicial local, descrita na arquitetura. Os cenários representam operação estabilizada, não o primeiro mês de vendas. A referência fiscal é 2026; o horizonte não constitui uma projeção fiscal para 2027.

## 2. Problema, público e proposta de valor

Configurações inconsistentes, ausência de documentação, protocolos inseguros e mudanças sem rastreabilidade dificultam o diagnóstico e aumentam a exposição a interrupções. O comprador esperado é o responsável por infraestrutura, TI/OT ou automação. Integradores podem contratar o serviço para apoiar sua carteira de clientes.

O valor proposto é reduzir o esforço de revisão e organizar evidências, prioridades, testes e planos de retorno. O relatório não certifica segurança, não garante disponibilidade e não substitui validação em campo. Uma configuração isolada não demonstra o estado operacional completo do equipamento.

### Oferta e alternativas

| Alternativa do cliente | Como atende à necessidade | Diferenciação proposta da Netrunner OT |
|---|---|---|
| Análise manual pela equipe interna | Usa conhecimento do ambiente | Regras reproduzíveis e formato padronizado de relatório |
| Consultoria pontual | Oferece análise especializada | Histórico recorrente e acompanhamento de ações |
| Ferramentas de inventário, backup e monitoramento | Acompanham ativos e eventos | Revisão de configuração contextualizada por consultor |

Essa comparação descreve categorias de solução. Não representa pesquisa de preços ou comprovação de superioridade frente a fornecedores. Antes do lançamento, o responsável pelo projeto deverá entrevistar pelo menos cinco potenciais compradores e levantar três propostas comparáveis de mercado, registrando escopo, valor, limites e data. Não foi estimado um tamanho de mercado sem evidência.

## 3. Operação, canais e receitas

1. Prospecção por integradores, indicação e conteúdo técnico.
2. Qualificação do fabricante, versões, quantidade de ativos e objetivo do diagnóstico.
3. Contratação e autorização para tratar configurações anonimizadas.
4. Upload manual, parser, regras determinísticas e triagem por IA.
5. Revisão humana, esclarecimento de dúvidas e liberação do relatório.
6. Acompanhamento das ações e renovação da assinatura.
7. Proposta independente para implantação, com backup, testes, janela e rollback.

O MVP terá controle comercial manual de contratos, franquias e horas. Integração com cobrança, API e white-label pertencem à evolução futura. Uma demonstração usará dados sintéticos, evitando o custo de revisão ilimitada de um plano gratuito.

### Capacidade dos cenários

| Premissa | Lean | Ideal |
|---|---:|---:|
| Clientes estabilizados | 20 | 60 |
| Mix Básico / Profissional | 15 / 5 | 30 / 30 |
| Equipamentos máximos nas franquias | 275 | 1.050 |
| Horas de revisão incluídas por mês | 50 | 180 |
| Capacidade técnica reservada proposta | 80 h/mês | 240 h/mês |
| Organização | Sócio gestor, desenvolvimento e revisão contratados | Sócio gestor, desenvolvimento ampliado e pelo menos dois revisores contratados |

O orçamento de revisão considera utilização integral das horas incluídas. A capacidade reservada é uma meta de disponibilidade, sem contratação mensal mínima no modelo. Se o prestador exigir pagamento pela reserva, o custo fixo deverá aumentar. O orçamento de desenvolvimento não é reutilizado como horas de revisão. A implantação das recomendações não consome a franquia de diagnóstico.

## 4. Custos, despesas e investimentos

Aplicando a aula **Custos e Despesas**, desenvolvimento, infraestrutura e revisão pertencem ao custo do serviço. Gestão, contabilidade e vendas são despesas. A classificação fixo/variável descreve o comportamento do gasto, enquanto direto/indireto indica a possibilidade de atribuí-lo ao serviço.

### 4.1 Recursos iniciais

| Item e memória da estimativa | Lean (R$) | Ideal (R$) | Tratamento no planejamento |
|---|---:|---:|---|
| Equipamentos e laboratório: 1 × 6.000 / 3 × 6.000 | 6.000 | 18.000 | Investimento em imobilizado |
| Formalização e implantação administrativa | 1.500 | 3.000 | Desembolso pré-operacional |
| Construção inicial: 200 h × 60 / 600 h × 80 | 12.000 | 48.000 | Desembolso de desenvolvimento |
| Revisão externa de segurança e privacidade | 0 | 12.000 | Serviço pré-operacional |
| Materiais de lançamento e configuração comercial | 1.500 | 4.000 | Despesa pré-operacional |
| **Subtotal para preparação** | **21.000** | **85.000** | |
| Capital de giro: três meses de gastos fixos | 24.000 | 75.000 | Reserva de caixa, não despesa |
| **Necessidade total de recursos** | **45.000** | **160.000** | Aporte próprio proposto, sem empréstimos |

O valor de desenvolvimento é orçamento para contratar trabalho, não afirmação de que o aplicativo ficará pronto nessas horas. O escopo deverá ser revisto após prototipação e estimativa técnica. No Lean, segurança será tratada no trabalho de desenvolvimento e revisão do sócio; a ausência de auditoria externa é uma limitação. O lançamento depende de validação mínima de isolamento, segredos e backups.

O planejamento não presume capitalização contábil de todo desenvolvimento. Esses valores saem do caixa antes da operação e não são lançados novamente nos gastos mensais. Para o imobilizado, considera-se vida útil gerencial de 36 meses e valor residual zero: depreciação de R$ 166,67/mês no Lean e R$ 500,00/mês no ideal. O tratamento contábil definitivo poderá diferir.

### 4.2 Gastos fixos mensais

| Item | Classificação | Lean (R$/mês) | Ideal (R$/mês) |
|---|---|---:|---:|
| Desenvolvimento e manutenção contratados | Custo fixo direto | 3.000 | 12.000 |
| Infraestrutura-base e backups | Custo fixo direto | 300 | 1.200 |
| Ferramentas de desenvolvimento e testes | Custo fixo direto | 200 | 800 |
| Gestão do sócio: pró-labore bruto | Despesa fixa administrativa | 1.500 | 3.000 |
| Contabilidade | Despesa fixa administrativa | 400 | 800 |
| Internet, energia e espaço compartilhado | Despesa fixa indireta | 400 | 1.200 |
| Marketing e vendas | Despesa fixa comercial | 1.500 | 4.500 |
| Apoio jurídico, segurança e administração | Despesa fixa administrativa | 700 | 1.500 |
| **Total mensal com desembolso** | | **8.000** | **25.000** |
| Depreciação dos equipamentos | Custo fixo sem desembolso | 166,67 | 500,00 |

O orçamento pressupõe prestadores externos por contrato e não empregados CLT. Valores de prestadores são totais das notas propostas, sem adicioná-los à folha para obter redução tributária. Retenções do pró-labore bruto não devem ser somadas novamente ao gasto. A adequação contratual e eventuais encargos adicionais precisam ser avaliados antes da operação. Se houver contratação CLT, férias, 13º, FGTS, benefícios e demais encargos exigirão novo orçamento.

Todos os gastos compartilhados são atribuídos integralmente à Netrunner OT, único produto do modelo. Se houver outras atividades, o rateio deverá considerar horas de uso ou dedicação comprovada. Infraestrutura-base é o mínimo mensal; consumo incremental aparece somente na tabela variável.

### 4.3 Gastos variáveis por assinatura

| Item | Básico (R$/cliente/mês) | Profissional (R$/cliente/mês) | Classificação |
|---|---:|---:|---|
| Revisão: 2 h ou 4 h × R$ 100/h | 200 | 400 | Custo variável direto |
| Processamento e armazenamento incrementais | 20 | 40 | Custo variável direto |
| Consumo estimado de IA | 10 | 20 | Custo variável direto |
| **Total variável do serviço** | **230** | **460** | |
| Meio de pagamento | 3% da receita | 3% da receita | Despesa financeira variável |
| Simples Nacional | Alíquota efetiva | Alíquota efetiva | Dedução tributária da receita |

A taxa de pagamento de 3% é uma hipótese média, não tarifa de fornecedor. IA e infraestrutura precisam ser medidas em testes com as configurações máximas admitidas. Horas excedentes não serão absorvidas silenciosamente: haverá orçamento e aceite prévios. Não há comissão comercial adicional no cenário-base.

## 5. Enquadramento tributário

Propõe-se **sociedade limitada optante pelo Simples Nacional**, se elegível, com receitas de software e consultoria segregadas conforme a atividade efetiva. Natureza jurídica, porte e regime tributário são conceitos distintos. CNAEs e códigos municipais serão definidos com contador após detalhar os contratos.

Para atividades sujeitas ao fator R, considera-se Anexo III quando a relação folha/receita dos últimos 12 meses atingir 28%; abaixo disso, Anexo V. O orçamento usa conservadoramente o **Anexo V**, sem presumir benefício por contratação de pessoas jurídicas. A composição legal da folha e as regras de início de atividade exigem apuração própria.

Na referência de 2026, os componentes pertinentes do DAS são IRPJ, CSLL, PIS/Pasep, Cofins, CPP e ISS. Não se soma ISS ou CPP novamente aos valores já abrangidos. Retenções e obrigações fora do DAS devem ser verificadas.

**Alíquota efetiva = (RBT12 × alíquota nominal − parcela a deduzir) ÷ RBT12.**

| Faixa do Anexo V utilizada no modelo | Nominal | Dedução (R$) |
|---|---:|---:|
| Até R$ 180.000 | 15,5% | 0 |
| Até R$ 360.000 | 18% | 4.500 |
| Até R$ 720.000 | 19,5% | 9.900 |
| Até R$ 1.800.000 | 20,5% | 17.100 |

Fonte: [LC 123/2006, art. 18 e Anexo V](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm). Tabela parcial suficiente para estes cenários.

### Aplicação ao modelo

- Lean: RBT12 hipotética de R$ 297.600; `(297.600 × 18% − 4.500) / 297.600 = 16,487903%`; DAS mensal estimado de **R$ 4.089**.
- Ideal: RBT12 hipotética de R$ 1.072.800; `(1.072.800 × 20,5% − 17.100) / 1.072.800 = 18,906040%`; DAS mensal estimado de **R$ 16.902**.

RBT12 foi aproximada por 12 meses iguais somente para análise estabilizada. O imposto real depende do histórico, segregação de receitas, início de atividade e regras vigentes. A operação não deve aplicar automaticamente essas alíquotas a qualquer mês.

**Transição tributária:** para 2027, a Receita Federal prevê decisão específica sobre recolhimento regular de IBS/CBS para optantes do Simples. Por isso, este orçamento de 2026 deverá ser atualizado antes da operação em outro exercício. Não se adicionou uma taxa genérica de IBS/CBS sobre o DAS. Ver [orientação da Receita Federal sobre 2027](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/setembro/simples-nacional-2027-entenda-os-novos-prazos-e-faca-sua-escolha-com-consciencia-e-tranquilidade).

## 6. Precificação e condições comerciais propostas

O modelo combina **planos por perfil e limite de uso**, com cobrança mensal por ambiente. A capacidade de pagamento e o valor percebido serão validados em entrevistas. Custos e margem constituem uma verificação de viabilidade, sem transformar horas já investidas em uma cobrança automática ao cliente. Essa abordagem segue a aula de Precificação.

| Oferta | Preço proposto | Limite e entrega |
|---|---:|---|
| Diagnóstico avulso | R$ 1.490 | Até 10 equipamentos de um ambiente, um ciclo e até 3 h de revisão |
| Assinatura Básico | R$ 990/mês | Até 10 equipamentos, um ambiente, um ciclo mensal e até 2 h de revisão |
| Assinatura Profissional | R$ 1.990/mês | Até 25 equipamentos, um ambiente, um ciclo mensal e até 4 h de revisão |
| Consultoria adicional | R$ 250/h | Mínimo de 4 h por contratação, orçamento e aceite prévios |
| Múltiplos ambientes ou maior volume | Sob proposta | Franquia, horas e infraestrutura dimensionadas previamente |

Um ciclo é um lote de até uma configuração por equipamento, com retorno de esclarecimentos dentro da franquia de horas. O relatório será liberado após revisão e informações suficientes. Caso a complexidade ultrapasse a franquia, o consultor apresentará escopo complementar antes de prosseguir. Os limites não significam que qualquer lote máximo poderá ser revisado adequadamente em duas horas; essa produtividade é hipótese a testar no piloto.

Os planos terão as mesmas regras técnicas e exigência de revisão humana. O preço maior remunera volume e horas, sem pressupor recursos ainda não construídos. SLA de emergência, atendimento 24×7, viagens, execução de mudanças e correções presenciais não integram a assinatura. Prazo de entrega será acordado após triagem. Cobrança mensal antecipada; cancelamento ao fim do ciclo, sem promessa de fidelização ou descontos anuais no cenário-base.

### Verificação de margem

No cenário Lean, o custo fixo rateado é `8.000 / 20 = R$ 400` por cliente. Com alíquota-base de 16,487903%, pagamento de 3% e margem de caixa desejada de 20% sobre a receita, o piso ilustrativo do Básico é:

`Preço = (230 + 400) / (1 − 0,16487903 − 0,03 − 0,20) = R$ 1.041,11`.

Assim, **R$ 990 não atinge isoladamente 20% de margem com esse rateio igualitário**. O preço é uma hipótese comercial sustentada pelo mix com o Profissional, cujo piso nas mesmas condições é R$ 1.421,20. Se as vendas se concentrarem no Básico, o orçamento e a meta de margem precisarão ser revistos. O preço final depende de validação de valor e disposição a pagar, não apenas dessa fórmula.

Diagnóstico avulso: custo direto proposto de R$ 330 (3 h × R$ 100 + R$ 30 de processamento). Consultoria: custo de R$ 100 por hora faturada. Com a alíquota do Lean e pagamento de 3%, as contribuições estimadas antes de gastos fixos são R$ 869,63 por diagnóstico e R$ 101,28 por hora de consultoria. Essas receitas adicionais não estão incluídas nas projeções de assinatura, evitando depender de projetos ainda não vendidos.

## 7. Resultado mensal estabilizado

| Indicador (R$/mês, exceto quando indicado) | Lean | Ideal |
|---|---:|---:|
| Clientes Básico / Profissional | 15 / 5 | 30 / 30 |
| Receita bruta recorrente | 24.800,00 | 89.400,00 |
| (−) DAS estimado | 4.089,00 | 16.902,00 |
| Receita após tributos | 20.711,00 | 72.498,00 |
| (−) Custos variáveis do serviço | 5.750,00 | 20.700,00 |
| (−) Custos fixos do serviço com desembolso | 3.500,00 | 14.000,00 |
| (−) Depreciação | 166,67 | 500,00 |
| **Resultado bruto do serviço** | **11.294,33** | **37.298,00** |
| (−) Despesas administrativas e comerciais fixas | 4.500,00 | 11.000,00 |
| (−) Despesas com meios de pagamento | 744,00 | 2.682,00 |
| **Resultado gerencial após depreciação** | **6.050,33** | **23.616,00** |
| (+) Depreciação, sem desembolso no mês | 166,67 | 500,00 |
| **Geração mensal de caixa operacional simplificada** | **6.217,00** | **24.116,00** |
| Margem de caixa sobre receita | 25,07% | 26,98% |

Essa é uma DRE gerencial simplificada, com uma conciliação de caixa. Não representa demonstração contábil formal nem lucro distribuível. Pressupõe recebimento integral, gastos pagos no mês, ausência de financiamentos, novos investimentos e variações de capital de giro. O pró-labore já está contemplado; distribuição de lucros não é gasto operacional projetado.

### Margem de contribuição e equilíbrio

`MC = receita − tributos sobre vendas − despesas de pagamento − custos variáveis`.

| Medida | Lean | Ideal |
|---|---:|---:|
| Contribuição mensal total | R$ 14.217,00 | R$ 49.116,00 |
| Contribuição média por cliente | R$ 710,85 | R$ 818,60 |
| Equilíbrio aproximado, mantendo alíquota do cenário-base | 12 clientes | 31 clientes |
| Equilíbrio de caixa recalculando faixa e mantendo mix exato | 12 clientes: 9 Básico + 3 Profissional | 30 clientes: 15 Básico + 15 Profissional |
| Caixa mensal nesse equilíbrio discreto | R$ 677,20 | R$ 117,50 |

A segunda conta procura o primeiro bloco inteiro de clientes com caixa não negativo e recalcula o tributo. No ideal, a alíquota menor perto do equilíbrio explica a diferença entre 30 e 31. O equilíbrio de caixa não cobre novos investimentos. Com depreciação, o ideal precisa do bloco seguinte, 32 clientes, para resultado contábil gerencial positivo.

### Reserva e retorno

O capital de giro cobre três meses de gastos fixos sem receita. Não garante financiar atrasos, desenvolvimento além do previsto ou uma aquisição lenta. Com cinco clientes (quatro Básico e um Profissional), o Lean gera aproximadamente **−R$ 4.530,75/mês** e consome a reserva. Uma previsão mensal de aquisição e cancelamento deverá anteceder a abertura.

Dividindo o aporte total pelo caixa estabilizado, o payback estático é de **7,24 meses no Lean** e **6,63 meses no ideal**. São indicadores a partir do patamar de vendas simulado, sem prazo de desenvolvimento, rampa comercial ou custo do capital. Não significam recuperação do investimento nesse prazo contado desde a criação da empresa.

## 8. Métricas e sensibilidade

| Métrica e hipótese | Lean | Ideal |
|---|---:|---:|
| ARPU = receita mensal / clientes | R$ 1.240,00 | R$ 1.490,00 |
| Novos clientes mensais para cálculo de CAC | 3 | 6 |
| CAC = marketing e vendas / novos clientes | R$ 500,00 | R$ 750,00 |
| Churn mensal hipotético | 3% | 3% |
| Permanência simplificada = 1 / churn | 33,33 meses | 33,33 meses |
| LTV de receita = ARPU / churn | R$ 41.333,33 | R$ 49.666,67 |
| LTV de contribuição = MC média / churn | R$ 23.695,00 | R$ 27.286,67 |

LTV não é lucro: a versão de contribuição ainda não desconta todos os gastos fixos, investimento ou valor do dinheiro no tempo. CAC considera somente o orçamento comercial informado. Horas comerciais do sócio deverão ser adicionadas quando mensuradas. Novos clientes e churn são hipóteses para indicadores, não uma projeção de crescimento reconciliada com a carteira estabilizada. A relação LTV/CAC elevada deve ser tratada como sinal de premissas ainda frágeis, não como tração comprovada.

| Sensibilidade isolada | Caixa Lean (R$/mês) | Caixa ideal (R$/mês) |
|---|---:|---:|
| Cenário-base | 6.217,00 | 24.116,00 |
| Preços 10% menores, mesmo volume e faixa recalculada | 4.257,80 | 17.276,90 |
| Hora do revisor sobe de R$ 100 para R$ 125 | 4.967,00 | 19.616,00 |

Desconto reduz margem sem reduzir trabalho de revisão. O risco mais relevante é precisar de mais horas por análise do que as franquias comportam. Em cada piloto serão medidos tempo de revisão, custo de IA, retrabalho, falsos positivos, disposição a pagar e conclusão das ações.

## 9. Riscos e critérios de expansão

| Risco | Resposta planejada |
|---|---|
| Demanda e preço não validados | Entrevistas e pilotos pagos antes de ampliar gastos fixos |
| Vazamento de configurações | Anonimização, segregação, controle de acesso e retenção definida |
| Recomendações incorretas | Evidências, revisão humana e teste antes de qualquer mudança |
| Consumo de IA ou horas excede orçamento | Medição por lote, franquia explícita e orçamento complementar |
| Dependência de poucos revisores | Segundo profissional habilitado no escopo e revisão por pares |
| Mudança tributária ou contratual | Revisão contábil antes da formalização e a cada mudança relevante |
| Atraso de desenvolvimento | MVP restrito e liberação condicionada aos critérios técnicos |

Passar ao ideal exige ao menos três meses de medição operacional, contratos capazes de sustentar os gastos ampliados, reserva compatível com a transição e validação de capacidade. A meta de 60 clientes não é demanda contratada. Segurança e revisão humana são requisitos também no Lean.

## 10. Plano de execução e relação com o projeto

| Fase proposta | Resultado verificável |
|---|---|
| Documentação e validação comercial | Contexto, especificação e plano alinhados; entrevistas registradas |
| Protótipo e orçamento técnico | Fluxo de upload e revisão demonstrável; estimativa de implementação |
| MVP e testes | Parser, pelo menos 20 regras, segregação e revisão funcionando |
| Piloto autorizado | Custos e tempos medidos; comparação com análise manual |
| Operação Lean | Contratos com franquias, cobrança e acompanhamento mensal |
| Expansão ideal | Capacidade e demanda comprovadas antes de contratar estrutura |

Ver [Documento de Contexto](Documento%20de%20Contexto.md) e [Especificação do Projeto](Especifica%C3%A7%C3%A3o%20do%20Projeto.md). O plano mantém suas hipóteses originais. Na Etapa 3, iniciou-se a implementação local; o escopo completo do MVP permanece pendente.

## 11. Referências e memória de cálculo

- Marcelo dos Reis. **01-Custos.pptx**, TAI III, PUC Minas, campus Poços de Caldas: slides 2–7 (classificações), 8–11 (custos do serviço) e 12–15 (despesas).
- Marcelo dos Reis. **02-Tributos.pptx**: slides 2–7 (categorias de tributos) e 8 (regime conforme segmento e faturamento). A aplicação específica usa as fontes legais indicadas na seção 5.
- Marcelo dos Reis. **04-Precificação.pptx**: slides 2–7 (valor e mercado), 8–10 (modelos), 11 (CAC, ARPU e LTV) e 12–14 (recorrência).
- Enunciado fornecido em **image(2).png**: atualização dos dois documentos, plano em Markdown, cenários Lean/ideal, tributos, precificação, link no README e envio do download do repositório ao Canvas.
- [Lei Complementar 123/2006](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm), art. 18 e Anexo V. Consulta em 01/10/2026.
- [Receita Federal: opções do Simples Nacional e IBS/CBS para 2027](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/setembro/simples-nacional-2027-entenda-os-novos-prazos-e-faca-sua-escolha-com-consciencia-e-tranquilidade). Consulta em 01/10/2026.

Os materiais de aula são referências fornecidas pelo responsável pelo projeto e não foram republicados neste repositório. Os valores do orçamento foram elaborados para o exercício. O script [calcular_cenarios.py](scripts/calcular_cenarios.py) reproduz as projeções principais sem dependências externas:

```bash
python scripts/calcular_cenarios.py
```

O cálculo usa precisão integral e arredonda apenas a apresentação. Tributos exibidos pelo script são projeções gerenciais, não guias de recolhimento.

## 12. Complemento da Etapa 3

O [fluxo de caixa](planilhas/Fluxo_de_Caixa.xlsx) acrescenta rampa de aquisição e prazos de recebimento/pagamento em horizonte relativo de 12 meses. Preserva preços e custos-base, mas usa reserva tributária conservadora editável em vez de reproduzir o DAS efetivo do cenário estabilizado. Assim, seus resultados não devem ser comparados como se fossem a mesma base de cálculo. O [guia das planilhas](planilhas/README.md) descreve a reconciliação e as novas hipóteses. A [SWOT](An%C3%A1lise%20de%20Ambientes%20%28SWOT%29.md) orienta as iniciativas do [Balanced Scorecard](planilhas/Balanced_Scorecard.xlsx).
