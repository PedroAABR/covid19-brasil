#Importando a tabela owid-codid-data para o codigo
df = pd.read_csv('/content/drive/MyDrive/Planilhas/owid-covid-data.csv', encoding='latin1')
#Selecionando apenas as colunas que possuem o Brasil
brasil = df[df['location'] == 'Brazil'].copy()
#Preenche colunas vazias com 0
brasil.fillna(0, inplace=True)
#Tira o limite de visualização de colunas
pd.set_option('display.max_columns', None)
#Transforma o índice padrão em índice de datas
brasil.set_index('date', inplace=False)
#Ordena por data
brasil.sort_index(inplace=True)

#Importa a tabela obito_cartorio para o codigo
df = pd.read_csv('/content/drive/MyDrive/Planilhas/obito_cartorio.csv', encoding='latin1')
mortes_estados = df
#Preenche colunas vazias com 0
mortes_estados.fillna(0, inplace=True)
#Tira o limite de visualização de colunas
pd.set_option('display.max_columns', None)
#Ordena por data
mortes_estados.sort_index(inplace=True)

#Importa a tabela para o codigo
df1 = pd.read_csv('/content/drive/MyDrive/Planilhas/2020_BR_Region_Mobility_Report.csv', encoding='latin1', low_memory=False)
df2 = pd.read_csv('/content/drive/MyDrive/Planilhas/2021_BR_Region_Mobility_Report.csv', encoding='latin1', low_memory=False)
df3 = pd.read_csv('/content/drive/MyDrive/Planilhas/2022_BR_Region_Mobility_Report.csv', encoding='latin1', low_memory=False)
#Unindo os dados verticalmente (se têm as mesmas colunas)
mobilidade = pd.concat([df1, df2, df3], ignore_index=True)
#Tira o limite de visualização de colunas
pd.set_option('display.max_columns', None)
#Remove múltiplas colunas
mobilidade = mobilidade.drop(['country_region_code', 'country_region', 'iso_3166_2_code','census_fips_code'], axis=1)
#Preenche colunas vazias com 0
mobilidade.fillna(0, inplace=True)
#Ordena por data
mobilidade.sort_index(inplace=True)

#Importa a tabela para o codigo
df = pd.read_csv('/content/drive/MyDrive/Planilhas/caso.csv', encoding='latin1')
casos_estados = df
#Remove múltiplas colunas
casos_estados = casos_estados.drop(['city', 'place_type', 'order_for_place','city_ibge_code'], axis=1)
#Tira o limite de visualização de colunas
pd.set_option('display.max_columns', None)
#Preenche colunas vazias com 0
casos_estados.fillna(0, inplace=True)
#Ordena por data
casos_estados.sort_index(inplace=True)

#Importa a tabela para o codigo
df1 = pd.read_csv('/content/drive/MyDrive/Planilhas/esus-vepi.LeitoOcupacao_2020.csv', encoding='latin1')
df2 = pd.read_csv('/content/drive/MyDrive/Planilhas/esus-vepi.LeitoOcupacao_2021.csv', encoding='latin1')
df3 = pd.read_csv('/content/drive/MyDrive/Planilhas/esus-vepi.LeitoOcupacao_2022.csv', encoding='latin1')
# Unindo os dados verticalmente (se têm as mesmas colunas)
ocupacao_hospital = pd.concat([df1, df2, df3], ignore_index=True)
# Remove múltiplas colunas
ocupacao_hospital = ocupacao_hospital.drop(['_id', 'cnes', '_p_usuario','estadoNotificacao','municipioNotificacao','municipio','excluido','validado'], axis=1)
#Tira o limite de visualização de colunas
pd.set_option('display.max_columns', None)
#Preenche colunas vazias com 0
ocupacao_hospital.fillna(0, inplace=True)
#Ordena por data
ocupacao_hospital.sort_index(inplace=True)

# Converter datas
brasil['date'] = pd.to_datetime(brasil['date'])
casos_estados['date'] = pd.to_datetime(casos_estados['date'])
mobilidade['date'] = pd.to_datetime(mobilidade['date'])
mortes_estados['date'] = pd.to_datetime(mortes_estados['date'])
ocupacao_hospital['_created_at'] = pd.to_datetime(ocupacao_hospital['_created_at'])

# Padronizar nomes de colunas (opcional)
brasil.columns = brasil.columns.str.lower().str.replace(" ", "_")
