## Relatório de Valuation: Projeto Hospfy

### 1. Pesquisa Conceitual sobre Valuation 

Para esta etapa, nosso grupo pesquisou os conceitos de *Valuation*, que é o processo de estimar o valor econômico do nosso negócio. O objetivo é determinar quanto o Hospfy vale, com base em sua capacidade de gerar resultados.

Analisamos as principais metodologias:

1.  **Múltiplos de Mercado:** Compara a empresa com concorrentes.
    * *Por que descartamos:* Inadequado para o Hospfy. Sendo uma startup em estágio inicial, não temos lucro para comparar e nem concorrentes diretos com dados públicos.

2.  **Valor Patrimonial (ou Contábil):** Soma os ativos e subtrai os passivos.
    * *Por que descartamos:* Também inadequado. O valor do Hospfy não está em ativos físicos, mas em nosso software e, principalmente, na nossa **capacidade de gerar receita futura**.

3.  **Fluxo de Caixa Descontado (FCD):** Projeta nossa capacidade futura de gerar caixa e traz esse valor para o presente, considerando os riscos.
    * ***Nosso Método Escolhido:*** Definimos o FCD como o método mais adequado, pois ele foca exatamente no potencial futuro do nosso negócio, que é a tese central do Hospfy.

---

### 2. Nossa Metodologia e Aplicação no Hospfy

#### 2.1. Aplicação do Valuation no Hospfy

Para aplicar o FCD, estabelecemos as seguintes premissas, que foram baseadas e validadas pelos dados da nossa projeção inicial.

**1. Premissa de Receita (Baseada na Imagem):**
Nossa projeção de Jan-Abr mostra a curva de tração inicial:
* Janeiro: R$ 4.200
* Fevereiro: R$ 9.100
* Março: R$ 15.400
* Abril: R$ 23.100

Esses dados validam que nosso **ponto de equilíbrio (break-even)** operacional é atingido muito próximo do Mês 4 (Saldo de -R$ 100,50).

Com base nisso, extrapolamos nossa receita para 5 anos. Assumimos que o break-even se consolida no Mês 5 e nosso crescimento continua forte, porém desacelerando percentualmente à medida que a base de clientes aumenta:

* **Receita Ano 1:** R$ 337.694 (Projeção dos 12 meses)
* **Receita Ano 2:** R$ 844.235 (Crescimento de 150%)
* **Receita Ano 3:** R$ 1.519.623 (Crescimento de 80%)
* **Receita Ano 4:** R$ 2.279.434 (Crescimento de 50%)
* **Receita Ano 5:** R$ 3.191.208 (Crescimento de 40%)

**2. Premissa de Estrutura de Custos:**
Utilizamos os percentuais do nosso plano de negócios detalhado:

* **Custos Variáveis (CV): 35,5% sobre a Receita Bruta**
    * *Composição:* 10% (Impostos) + 15% (Marketing) + 7% (Servidor Escala) + 3,5% (Taxas Pagamento).
* **Custos Fixos (CF): R$ 180.000,00/ano**
    * *Composição:* R$ 15.000,00/mês (Salários, Encargos, Benefícios, Servidor Base, Licenças, Contabilidade, Depreciação).
    * *Correção:* Aplicamos um reajuste de **5% ao ano** sobre os custos fixos (inflação) para maior realismo.

**3. Premissa de Desconto e Perpetuidade:**

* **Taxa de Desconto (TMA): 25% ao ano.** Definimos esta taxa para refletir o alto risco de uma startup de tecnologia no Brasil (competição, execução e mercado).
* **Crescimento na Perpetuidade (g): 6% ao ano.** É o crescimento modesto e sustentável que projetamos para o Hospfy após o Ano 5.

---

### 3. Nossa Projeção de Fluxo de Caixa (Relatório Sintético)

Com base nas premissas que definimos, nossa projeção de Fluxo de Caixa Livre (FCL) para o Hospfy é a seguinte:

| Métrica | Ano 0 | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Receita Bruta (A)** | R$ 0 | R$ 337.694 | R$ 844.235 | R$ 1.519.623 | R$ 2.279.434 | R$ 3.191.208 |
| (-) Custos Variáveis (35.5% de A) | R$ 0 | (R$ 119.881) | (R$ 299.703) | (R$ 539.466) | (R$ 809.200) | (R$ 1.132.889) |
| (-) Custos Fixos (B) | R$ 0 | (R$ 180.000) | (R$ 189.000) | (R$ 198.450) | (R$ 208.373) | (R$ 218.791) |
| **Fluxo de Caixa Operacional (FCO)** | R$ 0 | **R$ 37.813** | **R$ 355.532** | **R$ 781.707** | **R$ 1.261.861** | **R$ 1.839.528** |
| | | | | | | |
| (-) Investimento Inicial (Capex) | (R$ 112.100) | - | - | - | - | - |
| (-) Reinvestimento (CAPEX) | - | (R$ 0) | (R$ 5.000) | (R$ 5.000) | (R$ 10.000) | (R$ 10.000) |
| **Fluxo de Caixa Livre (FCL)** | **(R$ 112.100)** | **R$ 37.813** | **R$ 350.532** | **R$ 776.707** | **R$ 1.251.861** | **R$ 1.829.528** |
| | | | | | | |
| **Valor Presente (VP) do FCL** (TMA=25%) | (R$ 112.100) | **R$ 30.250** | **R$ 224.340** | **R$ 397.683** | **R$ 512.658** | **R$ 599.467** |

---

### 4. Resultado Final: O Valor do Hospfy

O valor final do nosso projeto é a soma dos Valores Presentes (VP) dos fluxos de caixa (Anos 1-5) mais o Valor Presente da Perpetuidade.

#### 🔹 A. Cálculo da Perpetuidade
Valor da perpetuidade ao final do Ano 5 (FCL Ano 6 / (TMA - g)):
`R$ 1.829.528 * (1.06) / (0.25 - 0.06) = R$ 10.207.699`

#### 🔹 B. Valor Presente (VP) da Perpetuidade
Trazendo o valor da perpetuidade para o Ano 0 (descontando 5 anos a 25%):
`R$ 10.207.699 / (1.25)^5 = R$ 3.344.471`

#### 🔹 C. Valuation (Soma dos VPs)
Soma do VP do FCL (Anos 1-5) + VP da Perpetuidade:
`30.250 + 224.340 + 397.683 + 512.658 + 599.467 + 3.344.471`
**Valuation (Valor da Empresa) = R$ 5.108.869**

#### 🔹 D. VPL (Valor Presente Líquido)
O VPL subtrai nosso investimento inicial do valor total, indicando a viabilidade do projeto.
`VPL = R$ 5.108.869 (Valuation) - R$ 112.100 (Invest. Inicial)`
**VPL = R$ 4.996.769**

### Conclusão da Nossa Análise

Nossa análise, utilizando a projeção de receita acelerada (que indica um **break-even operacional já no Mês 5**), demonstra que o projeto Hospfy tem um **Valuation estimado de R$ 5,1 milhões** e um VPL (Valor Presente Líquido) positivo de **R$ 4,99 milhões**.

**Observações Importantes do Grupo:**

* **Validação da Reserva:** A projeção inicial mostrou um saldo negativo de R$ -26.889 em Abril. Isso valida a importância da **Reserva Financeira de R$ 90.000,00** que planejamos, pois ela cobre confortavelmente este período de queima de caixa (runway).
* **Foco no Raciocínio:** Sabemos que este valor é uma estimativa direta da nossa projeção otimista de crescimento. A execução bem-sucedida desse crescimento é a premissa-chave para que este valor se realize, e esse foi o foco do nosso raciocínio financeiro.

---
