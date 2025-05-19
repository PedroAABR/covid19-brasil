# 🦠 Análise Exploratória da COVID-19 no Brasil
Análise aprofundada da pandemia de COVID-19 no Brasil, utilizando múltiplas fontes de dados para compreender a evolução de casos, óbitos, vacinação, mobilidade urbana, ocupação hospitalar e outros indicadores relevantes.

## 🎯 Objetivo

Realizar uma análise exploratória integrada de diferentes bases públicas sobre a COVID-19 no Brasil, com o intuito de gerar insights sobre a dinâmica da pandemia, avaliar impactos da vacinação, subnotificação, mobilidade urbana e capacidade hospitalar.

## 🔍 O que foi feito
### Leitura e limpeza de diversos datasets:

- Our World in Data (casos, óbitos, vacinação)

- Brasil.IO (casos e óbitos por estado)

- OpenDataSUS (ocupação hospitalar)

- Google Mobility Reports (mobilidade urbana)

- Cartórios (excesso de mortalidade)

- Padronização e tratamento de datas, colunas e índices.

- Remoção de colunas redundantes ou irrelevantes.

- Unificação e concatenação de dados por ano.

### Cálculo de métricas como:

- Média móvel de casos/mortes

- Excesso de mortalidade

- Ocupação hospitalar média

- Taxa de letalidade por estado

- Geração de visualizações descritivas e analíticas.

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

