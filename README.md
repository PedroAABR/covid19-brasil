# 🦠 Análise Exploratória da COVID-19 no Brasil
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/covid19-brasil-analysis/blob/main/notebooks/covid19_analysis.ipynb)

Análise aprofundada da pandemia de COVID-19 no Brasil, utilizando múltiplas fontes de dados para compreender a evolução de casos, óbitos, vacinação, mobilidade urbana, ocupação hospitalar e outros indicadores relevantes.

## 🎯 Objetivo

Realizar uma análise exploratória integrada de diferentes bases públicas sobre a COVID-19 no Brasil com o intuito de:

- Gerar insights sobre a dinâmica da pandemia;
- Avaliar os impactos da vacinação;
- Investigar possíveis subnotificações;
- Correlacionar mobilidade urbana com a evolução dos casos;
- Analisar a capacidade hospitalar ao longo do tempo.


## 🔍 O que foi feito

- 📥 Leitura e limpeza de datasets públicos:
  - Our World in Data (casos, óbitos, vacinação)
  - Brasil.IO (casos e óbitos por estado)
  - OpenDataSUS (ocupação hospitalar)
  - Google Mobility Reports (mobilidade urbana)
  - Cartórios (excesso de mortalidade)

- 🧹 Tratamento e padronização:
  - Conversão de datas, renomeação e unificação de colunas
  - Exclusão de colunas redundantes
  - Junção de dados multianuais

- 📊 Cálculo de métricas:
  - Média móvel de casos e mortes
  - Excesso de mortalidade
  - Ocupação média de UTIs
  - Taxa de letalidade por estado

- 📈 Visualizações descritivas e analíticas

## 📈 Principais Insights
| Dimensão              | Insight                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| **Casos e Mortes**    | Picos claros durante ondas da pandemia; mortalidade acompanha tendência.|
| **Vacinação**         | Início da vacinação coincide com queda nas mortes.                      |
| **Ocupação Hospitalar** | Alta ocupação de UTIs em momentos críticos da pandemia.                |
| **Mobilidade**        | Queda acentuada em locais de trabalho durante picos; mobilidade impactada. |
| **Excesso de Mortalidade** | 2020 apresentou excesso de óbitos significativo em comparação a 2019.   |
| **Estados com Maior Letalidade** | Algumas UF têm taxas de letalidade desproporcionalmente altas.        |
| **Correlações**       | Alta vacinação tende a reduzir mortes; mobilidade afeta dinâmica.       |

Para análises detalhadas, veja: [Análise Completa](./ANALYSIS.md)
## 🧠 Conclusões Gerais
#### - A vacinação em massa teve efeito visível na redução da mortalidade.

#### - Estados apresentaram variações significativas nos indicadores, sugerindo desigualdade regional.

#### - Houve momentos críticos com alta ocupação hospitalar e excesso de mortalidade.

#### - A mobilidade urbana respondeu diretamente às medidas de contenção.

#### - A análise integrada de dados de diferentes fontes enriquece o entendimento da crise sanitária.

## 🔗 Fontes dos Dados
[Our World in Data (OWID)](https://github.com/owid/covid-19-data/tree/master/public/data)

[Brasil.IO](https://brasil.io/dataset/covid19)

[OpenDataSUS](https://opendatasus.saude.gov.br/dataset/registro-de-ocupacao-hospitalar-covid-19)

[Google Mobility Reports](https://www.google.com/covid19/mobility/)


## 📁 Estrutura do Projeto
````
covid19-brasil/
├── data/             # Arquivos CSV com os dados brutos
├── notebooks/        # Jupyter Notebook com análises e visualizações
├── images/           # Gráficos exportados
├── ANALYSIS.md       # Análise detalhada com insights e interpretações
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação principal do projeto
````

## 🛠️ Principais Bibliotecas
#### - Python (pandas, numpy)
#### - Jupyter Notebook
#### - Matplotlib e Seaborn para visualização

## Sobre o autor
#### Pedro Augusto Alves Brandão — Data Analyst aspirante, apaixonado por transformar dados em decisões estratégicas.

## 📘 Acesse o notebook
👉 [Análise Covid19 no Brasil](https://colab.research.google.com/drive/1W_cGj3n7Rx-YZIDw2tVTtmnrQK50DpbY?usp=sharing)

## 📄 Licença
Projeto para uso educacional.

## 🔜 Próximos Passos
 Implementar uma versão interativa com Streamlit

 Utilizar Plotly para visualizações dinâmicas

 Aplicar modelagem preditiva com Machine Learning

 Disponibilizar dashboard público
## 💻 Como Executar
Clone este repositório:
````
git clone https://github.com/seu-usuario/covid19-brasil-analysis.git
````
Instale as dependências (recomenda-se uso do Google Colab):

- pandas

- matplotlib

- seaborn

- numpy

Execute o notebook principal no Colab para reproduzir as análises.

