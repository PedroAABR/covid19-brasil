# 📊 Evolução de Casos e Mortes no Brasil

<img src="reports/Evolução de Casos e Mortes no Brasil.png"/>


## 🔍 O que foi feito
Foi gerado um gráfico de linhas com séries temporais referentes à evolução da pandemia no Brasil:

- **new_cases_smoothed:** número de novos casos de COVID-19 suavizados por média móvel (7 dias);

- **new_deaths_smoothed:** número de novas mortes diárias também suavizadas pela média móvel.

A suavização das séries reduz o efeito de flutuações diárias e melhora a visualização de tendências e padrões ao longo do tempo.

## 📈 Principais Insights
1. **Múltiplas Ondas de Contágio**

O gráfico evidencia diversas ondas epidêmicas no Brasil entre 2020 e 2023:

   - A primeira onda, em meados de 2020, mostra um crescimento progressivo de casos e mortes.

   - A segunda onda, no primeiro semestre de 2021, foi mais intensa e letal, associada à variante Gama (P.1), originária de Manaus.

   - A terceira onda, no início de 2022, apresenta o maior pico de novos casos — fortemente vinculado à variante Ômicron. Apesar do recorde de infecções, as mortes não acompanharam na mesma 
     proporção, o que indica menor letalidade ou maior proteção vacinal.

2. **Descompasso entre Casos e Mortes**

Observa-se um atraso temporal entre os picos de casos e os de mortes, geralmente de algumas semanas. Esse comportamento é esperado devido à progressão natural da doença e tempo de agravamento clínico.

3. **Impacto da Vacinação (Pós-2021)**

Após o segundo semestre de 2021, nota-se que os picos de mortes diminuem consideravelmente, mesmo diante de novas ondas de contágio — evidenciando o impacto positivo da vacinação em massa.

4. **Tendência de Queda e Estabilização**

A partir do final de 2022 até 2024, a curva de novos casos e, principalmente, de mortes tende à estabilidade e baixos valores. Isso pode indicar o controle epidêmico, possivelmente sustentado por imunidade populacional (vacinal e natural) e mudanças no comportamento coletivo.
## 🧠 Conclusões Gerais
- A evolução da pandemia no Brasil apresenta padrões típicos de surtos sucessivos, impulsionados por novas variantes e oscilações no controle sanitário.

- A segunda onda foi a mais crítica em termos de mortalidade, exigindo respostas urgentes do sistema de saúde.

- A vacinação se consolidou como um divisor de águas, reduzindo expressivamente os óbitos mesmo diante de surtos com maior número de infectados.

- A curva demonstra a importância da vigilância contínua, políticas públicas ágeis e investimento em ciência, vacinação e comunicação pública durante crises sanitárias.

# 📊 Evolução da Vacinação no Brasil

<img src="reports/Pessoas Totalmente Vacinadas por 100 habitantes.png"/>

## 🔍 O que foi feito
Foi criado um gráfico de linha apresentando a evolução da métrica:

- **people_fully_vaccinated_per_hundred:** percentual da população brasileira com vacinação completa contra a COVID-19, por 100 habitantes.

O eixo horizontal representa o tempo (datas entre o início de 2021 até o início de 2023), enquanto o eixo vertical indica o percentual de cobertura vacinal. A visualização tem como objetivo monitorar a progressão da campanha de vacinação ao longo do tempo.

## 📈 Principais Insights
1. **Início Lento da Campanha Vacinal (Q1 e Q2 de 2021)**

Observa-se um crescimento bastante modesto no início da série (janeiro a abril de 2021), indicando que a campanha de vacinação começou de forma lenta — possivelmente devido à limitação de doses disponíveis e priorização por grupos de risco.

2. **Aceleração Significativa (Q3 de 2021)**
 
A partir de julho de 2021, nota-se uma curva acentuada de crescimento. Esse período marca a ampliação da vacinação para a população adulta em geral, com maior disponibilidade de doses e centros de vacinação.

3. **Pico de Crescimento e Saturação (Q4 de 2021 a Q2 de 2022)**
   
Entre setembro de 2021 e abril de 2022, a cobertura vacinal ultrapassa os 70%, chegando a cerca de 80% da população vacinada com o esquema completo. Após esse ponto, a curva se torna cada vez mais horizontal, indicando uma saturação na adesão vacinal — as pessoas que desejavam se vacinar já o fizeram.

4. **Estabilização e Estagnação (Após Q2 de 2022)**
   
A partir de meados de 2022 até o início de 2023, a taxa de vacinação praticamente não se altera, ficando em torno de 81%–82%. Isso pode indicar resistência vacinal, falta de campanhas ativas, ou barreiras logísticas para vacinação em populações remanescentes.

## 🧠 Conclusões Gerais
- A vacinação no Brasil apresentou um ritmo inicial lento, seguido de uma forte aceleração, atingindo níveis elevados de cobertura (acima de 80%) até meados de 2022.

- A curva evidencia um modelo típico de adesão populacional a campanhas massivas, com crescimento exponencial seguido de saturação.

- O alcançar de um platô vacinal pode ter sido influenciado por fatores como hesitação vacinal, desinformação ou dificuldades logísticas.

- A curva mostra que, apesar dos desafios iniciais, o Brasil conseguiu vacinar a maior parte da população — o que contribuiu significativamente para o controle da pandemia e redução de mortes a partir da segunda metade de 2021.

# 📊 Vacinação X Mortes no Brasil

<img src="reports/VacinaçãoXMortes.png"/>

## 🔍 O que foi feito
Foi gerado um gráfico de linha com a comparação temporal entre:

- **people_vaccinated_per_hundred:** percentual da população brasileira vacinada (ao menos uma dose);

- **new_deaths_smoothed:** número de novas mortes diárias por COVID-19, suavizadas por média móvel (7 dias).

O gráfico possibilita observar a correlação temporal entre o avanço da vacinação e a redução na mortalidade.

## 📈 Principais Insights
1. **Vacinação Inicia Após Primeiras Ondas**

A curva de vacinação inicia-se no começo de 2021, quando o país já havia enfrentado duas grandes ondas de mortes, com picos expressivos antes mesmo de qualquer cobertura vacinal relevante.

2. **Redução de Mortes com Aumento da Vacinação**

A partir do momento em que a população vacinada ultrapassa 20%–40%, nota-se uma redução progressiva e consistente no número de mortes, mesmo com a presença de novos picos de casos (observados em análises anteriores).

3. **Efeito da Imunização em Massa**

A fase de maior crescimento da curva de vacinação coincide com a queda mais acentuada da mortalidade, especialmente no segundo semestre de 2021 — evidenciando um efeito protetivo direto da imunização.

4. **Picos Posteriores com Menor Letalidade**

Em 2022, mesmo com surtos identificáveis em casos (não exibidos aqui), os picos de mortes são notadamente menores — sinalizando possível dissociação entre infecção e letalidade devido à vacinação, variantes menos agressivas (como a Ômicron), e maior preparo clínico.

## 🧠 Conclusões Gerais
- O gráfico corrobora a eficácia das vacinas na prevenção de mortes, sendo um indicativo robusto do impacto positivo da imunização em massa.

- A inversão de tendência entre as curvas (subida da vacinação e queda de mortes) reforça a necessidade de campanhas públicas bem estruturadas e políticas de saúde baseadas em evidências.

- Este tipo de análise pode ser um instrumento de comunicação estratégica em saúde pública para combater hesitação vacinal, utilizando dados visuais para demonstrar impactos concretos.

- A continuidade da vigilância epidemiológica e reforço de doses podem ser fundamentais para manter os níveis de mortalidade baixos em futuras ondas epidêmicas.

# 📊 Ocupação Média de UTIs por COVID-19

<img src="reports/OcupaçãoMédiaUTI.png"/>

## 🔍 O que foi feito
Foi gerado um gráfico de barras com a série temporal da variável:

- **ocupacao_hospital.groupby('_created_at')['ocupacaoCovidUti'].mean().dropna():** representando a média diária de leitos ocupados em Unidades de Terapia Intensiva por pacientes com COVID.

O eixo horizontal representa as datas (_created_at), entre 2020 e 2025, enquanto o eixo vertical indica o número médio de leitos ocupados por dia.

## 📈 Principais Insights
1. **Baixa Ocupação no Início da Pandemia**

Até meados de 2020, observa-se uma ocupação baixa e instável, refletindo os primeiros estágios da pandemia, quando os casos ainda estavam se espalhando gradualmente.

2. **Picos Críticos em 2021 e 2022**

Entre 2021 e 2022, há picos intensos de ocupação com valores que ultrapassam 200 e até 1000 leitos ocupados em determinados dias. Esses picos correspondem aos períodos mais críticos da pandemia:

   - O primeiro grande pico coincide com a segunda onda da COVID-19 no Brasil, impulsionada pela variante Gama.

   - O segundo pico, ainda mais acentuado, está possivelmente associado à variante Ômicron, com alta transmissibilidade.

3. **Queda Progressiva Pós-2022**

A partir do segundo semestre de 2022, observa-se uma queda consistente da ocupação média de UTIs, que se mantém próxima de zero ao longo de 2023 e 2024. Essa tendência está fortemente associada:

   - ao avanço da vacinação em massa;

   - à maior capacidade de resposta hospitalar;

   - e à redução da gravidade clínica nas novas variantes.

4. **Valores Atípicos/Anômalos**

Os dois picos acima de 1000 chamam atenção e podem indicar erros de registro ou consolidação de dados acumulados em um único dia, devendo ser investigados como possíveis outliers.

## 🧠 Conclusões Gerais
- O gráfico evidencia a pressão extrema sobre o sistema de saúde brasileiro durante os períodos críticos da pandemia, com destaque para 2021 e início de 2022.

- A forte queda na ocupação hospitalar em UTIs após o início da vacinação reflete o impacto positivo da imunização, da testagem precoce e da eficácia dos tratamentos clínicos.

- A estabilização da ocupação em níveis próximos de zero em 2023–2024 sugere efetivo controle epidemiológico, tornando a pandemia uma condição endêmica.

- Indicadores como esse são fundamentais para subsidiar decisões políticas e estratégias de contenção, além de dimensionar a capacidade hospitalar em futuras emergências sanitárias.

# 📊 Excesso de Mortalidade por Semana Epidemiológica no Brasil

<img src="reports/ExcessoMortalidadeSemana.png"/>

## 🔍 O que foi feito
Foi gerado um gráfico de linha com faixa de variação (intervalo de confiança ou desvio padrão), apresentando o excesso de mortalidade semanal ao longo do ano de 2020. A variável principal representada é:

- **mortes_estados['deaths_total_2020'] - mortes_estados['deaths_total_2019']:** diferença entre o número de óbitos observados e o número de óbitos esperados, estimado a partir de médias históricas para cada semana epidemiológica.

O eixo horizontal representa a semana epidemiológica (1 a 53), enquanto o eixo vertical mostra a quantidade acumulada de óbitos excedentes.

## 📈 Principais Insights
1. **Crescimento Gradual Inicial (Semanas 1–18)**

Até a 18ª semana, os valores de óbitos em excesso permanecem baixos e relativamente estáveis, com pequena variação — indicando que ainda não havia impacto significativo da COVID-19 nos registros de mortalidade.

2. **Aumento Acelerado (Semanas 19–30)**

A partir da 19ª semana, observa-se um crescimento exponencial no excesso de mortes, atingindo cerca de 3.000 óbitos excedentes por volta da 30ª semana. Esse período coincide com o avanço mais agressivo da pandemia no Brasil durante o primeiro semestre de 2020.

3. **Manutenção em Alta (Semanas 30–50)**

Mesmo com alguma desaceleração, os óbitos em excesso continuam crescendo de forma constante, ultrapassando 7.000 mortes excedentes até a 50ª semana. Isso indica um impacto persistente e elevado na mortalidade geral do país.

4. **Faixa de Incerteza Considerável**

A área sombreada em torno da linha principal sugere que há variabilidade nas estimativas semanais, o que pode ser devido a diferenças regionais, atrasos na notificação ou incertezas no modelo de expectativa histórica.

## 🧠 Conclusões Gerais
- O gráfico demonstra com clareza o efeito devastador da pandemia de COVID-19 no Brasil em 2020, com milhares de mortes a mais do que o esperado em condições normais.

- A métrica de excesso de mortalidade é crucial para mensurar o impacto real de crises sanitárias, inclusive considerando mortes indiretas (ex: sobrecarga hospitalar, falta de atendimento, subnotificação).

- A aceleração a partir da 20ª semana é compatível com a explosão dos casos e mortes reportadas oficialmente, confirmando a correlação entre a disseminação do vírus e o aumento expressivo da mortalidade.

- Esta análise é fundamental para reforçar a importância de vigilância epidemiológica robusta, planejamento de resposta a crises e transparência na notificação de dados de saúde pública.

# 📊 Mudança na Mobilidade para Locais de Trabalho no Brasil

<img src="reports/Mobilidade para Locais de Trabalho.png"/>

## 🔍 O que foi feito

Foi gerado um gráfico de linha temporal com os dados de variação percentual na mobilidade de pessoas em direção aos **locais de trabalho**, com base nos dados do Google Mobility Reports. A métrica representa a mudança percentual em relação à linha de base (período pré-pandêmico).

- **Variável analisada**: `workplaces_percent_change_from_baseline`  
- **Período**: De janeiro de 2020 até o final de 2022  
- **Eixo X**: Datas diárias  
- **Eixo Y**: Variação percentual na mobilidade

## 📈 Principais Insights

1. **Queda Acentuada no Início da Pandemia (março–abril de 2020)**  
   - A mobilidade caiu drasticamente, atingindo **valores abaixo de -60%**, resultado direto do início do isolamento social e do fechamento de escritórios e comércios.

2. **Oscilações e Recuperações Parciais em 2020 e 2021**  
   - A partir do segundo semestre de 2020, há **oscilações semanais**, mas a mobilidade segue abaixo de zero, com **quedas mais intensas em finais de semana e feriados**.
   - Em 2021, nota-se uma **recuperação gradual**, embora ainda com quedas eventuais associadas a novas ondas da pandemia e medidas restritivas.

3. **Recuperação Acelerada a partir de 2022**  
   - A mobilidade volta a valores **próximos ou acima de 0%**, indicando o **retorno progressivo das atividades presenciais**, especialmente após a vacinação em massa.
   - Picos positivos acima de 40% evidenciam **reabertura econômica** e flexibilização das medidas de contenção.

4. **Manutenção de Padrões Semanais**  
   - As variações negativas regulares indicam a **redução da mobilidade em finais de semana**, característica típica dos padrões de comportamento, e que se manteve mesmo após o retorno gradual.

## 🧠 Conclusões Gerais

- A mobilidade para locais de trabalho foi **diretamente impactada pelas medidas de isolamento social**, especialmente no início da pandemia.
- O gráfico mostra como o **comportamento da população foi alterado** ao longo do tempo, com fases de retração e posterior recuperação.
- A partir de 2022, observa-se uma **normalização gradual da mobilidade**, compatível com o avanço da vacinação, diminuição dos casos graves e **reabertura do mercado de trabalho presencial**.
- A análise dessa métrica é essencial para compreender os efeitos sociais e econômicos da pandemia e pode ser usada para **correlação com dados de contágio e produtividade**.



