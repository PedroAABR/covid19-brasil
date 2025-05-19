#Evolução de casos e mortes
plt.figure(figsize=(12, 5))
sns.lineplot(data=brasil, x='date', y='new_cases_smoothed', label='Novos casos', alpha=0.7)
sns.lineplot(data=brasil, x='date', y='new_deaths_smoothed', label='Novas mortes', alpha=0.7)
plt.title("Evolução de Casos e Mortes no Brasil")
plt.xlabel("Data")
plt.ylabel("Número")
plt.legend()
plt.grid(True)

#Vacinação
plt.figure(figsize=(12, 5))
sns.lineplot(data=brasil, x='date', y='people_fully_vaccinated_per_hundred')
plt.title("Pessoas Totalmente Vacinadas por 100 habitantes")
plt.ylabel("Percentual (%)")
plt.grid(True)

#Testagem e Subnotificação
plt.figure(figsize=(10, 5))
sns.lineplot(data=brasil, x='date', y='positive_rate')
plt.title("Taxa de Positividade dos Testes")
plt.ylabel("Taxa de Positividade")
plt.grid(True)

#Vacinação vs Casos/Mortes
plt.figure(figsize=(10, 5))
sns.lineplot(data=brasil, x='date', y='people_vaccinated_per_hundred', label="Vacinados (%)")
sns.lineplot(data=brasil, x='date', y='new_deaths_smoothed', label="Novas mortes")
plt.title("Vacinação vs Mortes")
plt.legend()
plt.grid(True)

#Ocupação de UTI
df_uti = ocupacao_hospital.groupby('_created_at')['ocupacaoCovidUti'].mean().dropna()

plt.figure(figsize=(10, 5))
df_uti.plot()
plt.title("Ocupação Média de UTI por COVID")
plt.ylabel("Ocupação Média")
plt.grid(True)

#Excesso de Mortalidade
mortes_estados['excesso'] = mortes_estados['deaths_total_2020'] - mortes_estados['deaths_total_2019']

plt.figure(figsize=(10, 5))
sns.lineplot(data=mortes_estados, x='epidemiological_week_2020', y='excesso')
plt.title("Excesso de Mortalidade por Semana Epidemiológica")
plt.ylabel("Óbitos em Excesso")
plt.grid(True)

#Mobilidade Urbana
plt.figure(figsize=(10, 5))
sns.lineplot(data=mobilidade, x='date', y='workplaces_percent_change_from_baseline')
plt.title("Mudança na Mobilidade para Locais de Trabalho")
plt.ylabel("Variação (%)")
plt.grid(True)

# Pegar última entrada por estado
ultimos_estados = casos_estados.sort_values('date').groupby('state').last().reset_index()

# Remover possíveis entradas agregadas como 'TOTAL'
ultimos_estados = ultimos_estados[ultimos_estados['state'].str.len() == 2]

# Remover valores nulos e ordenar
top_mortalidade = ultimos_estados.dropna(subset=['death_rate']).sort_values('death_rate', ascending=False)

# Gráfico atualizado
plt.figure(figsize=(10, 8))
sns.barplot(data=top_mortalidade.head(10), x='state', y='death_rate', palette='Reds')
plt.title("Top 10 Estados com Maior Taxa de Letalidade")
plt.ylabel("Taxa de Letalidade")
plt.xlabel("Estado")
plt.grid(True)

#Associações e Correlações
df_corr = brasil[['people_fully_vaccinated_per_hundred', 'new_deaths_smoothed']].dropna()

sns.lmplot(data=df_corr, x='people_fully_vaccinated_per_hundred', y='new_deaths_smoothed')
plt.title("Correlação: Vacinação vs Mortes")

#Casos por mês no Brasil
#Agregando casos por mês
brasil['mes_ano'] = brasil['date'].dt.to_period('M')
casos_mensais = brasil.groupby('mes_ano')['new_cases'].sum()

plt.figure(figsize=(12, 5))
casos_mensais.plot(kind='line', marker='o')
plt.title("Casos Mensais de COVID-19 no Brasil")
plt.xlabel("Mês")
plt.ylabel("Número de Casos")
plt.grid(True)

# Top 5 estados com mais casos/óbitos (total acumulado)
# Agrupando dados acumulados por estado
casos_estado_total = casos_estados.groupby('state')[['confirmed', 'deaths']].sum().sort_values('confirmed', ascending=False)

top5_estados = casos_estado_total.head(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top5_estados, x='state', y='confirmed', color='steelblue', label="Casos")
sns.barplot(data=top5_estados, x='state', y='deaths', color='red', label="Óbitos")
plt.title("Top 5 Estados com Mais Casos e Óbitos")
plt.ylabel("Total Acumulado")
plt.legend()

# Heatmap de Correlação
# Selecionar colunas numéricas relevantes
cols_correlacao = ['new_cases', 'new_deaths', 'total_tests', 'positive_rate', 
                   'people_vaccinated', 'people_fully_vaccinated', 'reproduction_rate']

df_corr = brasil[cols_correlacao].dropna()
corr_matrix = df_corr.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Mapa de Correlação entre Variáveis")

# Boxplot de Casos por Mês (Sazonalidade)
brasil['ano_mes'] = brasil['date'].dt.to_period('M')
brasil_boxplot = brasil[['ano_mes', 'new_cases']].dropna()

plt.figure(figsize=(30, 6))
sns.boxplot(data=brasil_boxplot, x='ano_mes', y='new_cases')
plt.xticks(rotation=45)
plt.title("Boxplot de Casos Novos por Mês")
plt.ylabel("Novos Casos")

#Média Móvel de 7 Dias (Rolling Average)
brasil['media_movel_casos'] = brasil['new_cases'].rolling(7).mean()
brasil['media_movel_mortes'] = brasil['new_deaths'].rolling(7).mean()

plt.figure(figsize=(12, 5))
sns.lineplot(data=brasil, x='date', y='media_movel_casos', label="Casos (7 dias)")
sns.lineplot(data=brasil, x='date', y='media_movel_mortes', label="Mortes (7 dias)")
plt.title("Média Móvel de Casos e Mortes (7 dias)")
plt.xlabel("Data")
plt.ylabel("Número")
plt.legend()
plt.grid(True)

# Mapa de calor da evolução semanal de óbitos por estado
heatmap_data = mortes_estados.pivot_table(
    index='state',
    columns='epidemiological_week_2020',
    values='new_deaths_covid19',
    aggfunc='sum'
)

plt.figure(figsize=(16, 10))
sns.heatmap(heatmap_data, cmap='Reds', linewidths=.5)
plt.title("Evolução Semanal de Óbitos por COVID-19 por Estado")
plt.xlabel("Semana Epidemiológica - 2020")
plt.ylabel("Estado")

# Ocupação hospitalar total ao longo do tempo (UTI + Clínica)
ocupacao_hospital['_created_at'] = pd.to_datetime(ocupacao_hospital['_created_at'])
ocupacao_hospital['ocupacao_total'] = ocupacao_hospital['ocupacaoCovidUti'] + ocupacao_hospital['ocupacaoCovidCli']

df_ocupacao = ocupacao_hospital.groupby('_created_at')['ocupacao_total'].mean()

plt.figure(figsize=(12, 5))
df_ocupacao.plot()
plt.title("Ocupação Total Média de Leitos por COVID no Tempo")
plt.ylabel("Leitos Ocupados (Média)")
plt.xlabel("Data")
plt.grid(True)

#Taxa de Letalidade por Estado com População Estimada
# Filtrar últimas entradas válidas
casos_estados['date'] = pd.to_datetime(casos_estados['date'])
ultimos = casos_estados.sort_values('date').groupby('state').last().reset_index()
ultimos = ultimos[ultimos['state'].str.len() == 2]

# Plot com tamanho proporcional à população
plt.figure(figsize=(12, 6))
sns.scatterplot(data=ultimos, x='confirmed_per_100k_inhabitants', y='death_rate',
                size='estimated_population', hue='state', sizes=(50, 1000), legend=False)

plt.title("Taxa de Letalidade vs Casos por 100k habitantes (tamanho = população)")
plt.xlabel("Casos por 100 mil habitantes")
plt.ylabel("Taxa de Letalidade")
plt.grid(True)

#Impacto da Vacinação na Mortalidade ao longo do tempo
fig, ax1 = plt.subplots(figsize=(12, 5))

ax2 = ax1.twinx()

sns.lineplot(data=brasil, x='date', y='people_fully_vaccinated_per_hundred', color='green', ax=ax1, label='Vacinados (%)')
sns.lineplot(data=brasil, x='date', y='new_deaths_smoothed', color='red', ax=ax2, label='Mortes (média móvel)')

ax1.set_ylabel('Pessoas Totalmente Vacinadas (%)', color='green')
ax2.set_ylabel('Novas Mortes (média móvel)', color='red')
ax1.set_title("Evolução da Vacinação vs Mortes")

#Mudança de mobilidade por categoria
mobilidade['date'] = pd.to_datetime(mobilidade['date'])
df_mob = mobilidade.groupby('date').mean(numeric_only=True)

plt.figure(figsize=(14, 6))
for coluna in df_mob.columns:
    if 'percent_change' in coluna:
        sns.lineplot(data=df_mob, x=df_mob.index, y=coluna, label=coluna.split('_percent')[0])

plt.axhline(0, color='gray', linestyle='--')
plt.title("Mudança na Mobilidade por Tipo de Local")
plt.ylabel("Variação em relação à linha de base (%)")
plt.legend(loc='lower left')
