# 📊 Evolução de Casos e Mortes no Brasil

<img src="reports/Evolução de Casos e Mortes no Brasil.png"/>


## 🔍 O que foi feito
Foi gerado um gráfico de linhas com as séries temporais:

- **new_cases_smoothed:** novos casos diários suavizados (média móvel de 7 dias);

- **new_deaths_smoothed:** novas mortes diárias suavizadas (média móvel de 7 dias).

A suavização tem como objetivo reduzir ruídos de variações diárias e destacar tendências consistentes.

## 📈 Principais Insights
1. **Múltiplas Ondas da Pandemia**
   
É possível observar claramente três grandes ondas de infecção, com seus respectivos picos de novos casos e mortes.

   - A segunda onda (início de 2021) foi a mais letal, coincidente com a variante Gama.

   - A terceira onda (início de 2022) teve alto número de casos, mas menor letalidade, associada à variante Ômicron.

2. **Defasagem entre Casos e Mortes**
   
Existe um atraso de alguns dias a semanas entre o pico de casos e o pico de mortes, refletindo o tempo de progressão da doença.

3. **Efeito da Vacinação**
   
A partir de meados de 2021, observa-se uma desaceleração clara na curva de mortes, mesmo com novos aumentos de casos — sugerindo efeito positivo da vacinação em massa.

4. **Estabilização no Final do Período**
   
As curvas tendem à estabilidade em 2022, refletindo possível controle pandêmico com vacinação, imunidade coletiva e maior preparo do sistema de saúde.

## 🧠 Conclusões Gerais
- O Brasil enfrentou momentos críticos ao longo da pandemia, refletidos em picos sucessivos de infecção e mortalidade.

- A análise temporal evidencia a importância de políticas públicas, vacinação e intervenções precoces.

- O impacto das variantes é perceptível na variação entre letalidade e contágio.

- A similaridade entre as curvas de casos e mortes reafirma a necessidade de medidas preventivas em estágios iniciais das ondas.

# 📊 Evolução da Vacinação no Brasil

<img src="reports/Pessoas Totalmente Vacinadas por 100 habitantes.png"/>

# 🔍 O que foi feito
Foi construído um gráfico de linha com a métrica:

- **people_fully_vaccinated_per_hundred:** representa o número de pessoas com o esquema vacinal completo a cada 100 habitantes, equivalente ao percentual da população totalmente vacinada.

Foram tratados dados ausentes e interpoladas lacunas visíveis para manter a visualização consistente sempre que possível, sem comprometer a integridade da análise.

# 📈 Principais Insights
1. **Início e Aceleração da Vacinação**

- A vacinação começou efetivamente em meados de janeiro de 2021, com crescimento lento nos primeiros meses.

- A partir do segundo semestre de 2021, observa-se uma aceleração significativa na curva de vacinação.

2. **Alta Cobertura Vacinal em 2022**

- O percentual de pessoas totalmente vacinadas ultrapassou 80% da população ao final de 2022 — um dado relevante considerando o tamanho populacional do Brasil.

3. **Falhas e Lacunas nos Dados**

- A série apresenta interrupções e valores ausentes frequentes a partir de 2022, especialmente no ano de 2023, possivelmente por falhas de reporte nos repositórios oficiais.

4. **Fim da Atualização**

- A curva parece interrompida após o início de 2023, indicando que os dados deixaram de ser atualizados ou passaram a ser consolidados de outra forma.


