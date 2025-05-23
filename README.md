# Engenharia e Análise de Dados E-commerce Brasileiro - Teste Técnico triggo.ai

## Descrição do Projeto
Este projeto contém a solução para o teste técnico do Programa Trainee triggo.ai de Excelência em Engenharia de Dados e DataOps 2025. 
A análise é baseada no conjunto de dados "Brazilian E-commerce Public Dataset by Olist" disponível no Kaggle.

O projeto analisa dados de e-commerce brasileiro para extrair insights sobre vendas, comportamento de clientes, desempenho de entregas e satisfação de clientes, oferecendo uma visão completa das operações e oportunidades de negócio.

## Arquitetura Medallion
Este projeto segue a arquitetura Medallion (também conhecida como Arquitetura Delta Lake) para processamento de dados, que organiza o fluxo de dados em camadas progressivamente mais refinadas:

```mermaid
flowchart TB
    A[Landing Zone] -->|Ingestão| B[Bronze]
    B -->|Limpeza| C[Silver]
    C -->|Agregação| D[Gold]
    D -->|Análise| E[Insights]
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000
    style B fill:#cd7f32,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c0c0c0,stroke:#333,stroke-width:2px,color:#000
    style D fill:#ffd700,stroke:#333,stroke-width:2px,color:#000
    style E fill:#99ff99,stroke:#333,stroke-width:2px,color:#000
```

1. **Landing Zone**: Dados brutos, exatamente como foram obtidos do Kaggle
2. **Bronze**: Dados ingeridos com validações básicas e metadados
3. **Silver**: Dados limpos, normalizados e transformados
4. **Gold**: Dados agregados e prontos para análise de negócios e visualização

## Estrutura do Projeto

```mermaid
graph TD
    A[data_engineering] --> B[dataset]
    A --> C[bronze]
    A --> D[silver]
    A --> E[gold]
    A --> F[notebooks]
    A --> G[README.md]
    
    F --> F1[1_landing_to_bronze.ipynb]
    F --> F2[2_bronze_to_silver.ipynb]
    F --> F3[3_silver_to_gold.ipynb]
    F --> F4[4_analise_exploratoria.ipynb]
    F --> F5[5_solucao_problemas.ipynb]
    F --> F6[6_visualizacao_dashboards.ipynb]
    
    style A fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style B fill:#ffcc99,stroke:#333,stroke-width:1px,color:#000
    style C fill:#cd7f32,stroke:#333,stroke-width:1px,color:#000
    style D fill:#c0c0c0,stroke:#333,stroke-width:1px,color:#000
    style E fill:#ffd700,stroke:#333,stroke-width:1px,color:#000
    style F fill:#99ccff,stroke:#333,stroke-width:1px,color:#000
    style G fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F1 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F2 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F3 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F4 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F5 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F6 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
```

```
data_engineering/
│
├── dataset/                    # Diretório para armazenar os arquivos CSV do dataset (Landing Zone)
├── bronze/                     # Camada Bronze - Dados ingeridos formatados em SQLite
├── silver/                     # Camada Silver - Dados limpos e transformados
├── gold/                       # Camada Gold - Dados agregados e modelados para análise
│
├── notebooks/                  # Jupyter Notebooks para análises
│   ├── 1_landing_to_bronze.ipynb     # Ingestão dos dados brutos para a camada bronze
│   ├── 2_bronze_to_silver.ipynb      # Transformação dos dados bronze para silver
│   ├── 3_silver_to_gold.ipynb        # Agregação dos dados silver para gold
│   ├── 4_analise_exploratoria.ipynb  # Análise exploratória de dados (EDA)
│   ├── 5_solucao_problemas.ipynb     # Solução para os problemas de negócio
│   └── 6_visualizacao_dashboards.ipynb # Criação de visualizações e dashboards
│
└── README.md                   # Documentação do projeto
```

```mermaid
flowchart LR
    A[Clone do Repositório] --> B[Download Dataset Kaggle]
    B --> C[Extrair CSVs para /dataset]
    C --> D[Executar Notebook 1]
    D --> E[Executar Notebook 2]
    E --> F[Executar Notebook 3]
    F --> G[Executar Notebooks de Análise]
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:1px,color:#000
    style B fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style C fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style D fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style E fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style F fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style G fill:#99ff99,stroke:#333,stroke-width:1px,color:#000
```

## Configuração do Ambiente

1. Clone este repositório

2. Baixe o dataset do Kaggle: [Brazilian E-commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

3. Extraia os arquivos CSV para a pasta `dataset/` (Landing Zone)

4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute os notebooks na ordem numérica para processar os dados através das camadas Medallion:
   - `1_landing_to_bronze.ipynb`
   - `2_bronze_to_silver.ipynb`
   - `3_silver_to_gold.ipynb`

6. Após o processamento, execute os notebooks de análise:
   - `4_analise_exploratoria.ipynb`
   - `5_solucao_problemas.ipynb`
   - `6_visualizacao_dashboards.ipynb`

## Fluxo de Processamento de Dados e Análise

```mermaid
flowchart TD
    subgraph Processing ["Processamento de Dados (Camadas Medallion)"]
        A[Landing Zone:<br>CSV Files] -->|Notebook 1| B[Bronze Layer:<br>SQLite Tables]
        B -->|Notebook 2| C[Silver Layer:<br>Normalized Tables]
        C -->|Notebook 3| D[Gold Layer:<br>Star Schema]
    end
    
    subgraph Analysis ["Análise de Dados e Insights"]
        D -->|Notebook 4| E[Análise Exploratória]
        D -->|Notebook 5| F[Solução de Problemas]
        D -->|Notebook 6| G[Dashboards]
    end
    
    E --> H[Insights de Negócio]
    F --> H
    G --> H
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:1px,color:#000
    style B fill:#cd7f32,stroke:#333,stroke-width:1px,color:#000
    style C fill:#c0c0c0,stroke:#333,stroke-width:1px,color:#000
    style D fill:#ffd700,stroke:#333,stroke-width:1px,color:#000
    style E fill:#99ccff,stroke:#333,stroke-width:1px,color:#000
    style F fill:#99ccff,stroke:#333,stroke-width:1px,color:#000
    style G fill:#99ccff,stroke:#333,stroke-width:1px,color:#000
    style H fill:#99ff99,stroke:#333,stroke-width:1px,color:#000
    style Processing fill:#f5f5f5,stroke:#666,stroke-width:2px,color:#000
    style Analysis fill:#f5f5f5,stroke:#666,stroke-width:2px,color:#000
```

## Descrição dos Notebooks e Camadas Medallion

### 1. Landing Zone para Bronze (1_landing_to_bronze.ipynb)
- **Objetivo**: Ingestão inicial dos dados brutos para um formato estruturado
- **Processos**:
  - Ingestão dos arquivos CSV brutos da Landing Zone
  - Validações básicas (schema, tipos de dados)
  - Adição de metadados (timestamp de ingestão, fonte)
  - Registro de problemas de qualidade sem correção
- **Saída**: Banco de dados SQLite com os dados brutos estruturados

### 2. Bronze para Silver (2_bronze_to_silver.ipynb)
- **Objetivo**: Transformar os dados brutos em dados limpos e estruturados
- **Processos**:
  - Limpeza e tratamento de valores nulos/inválidos
  - Normalização de colunas e padronização de formatos
  - Transformações e enriquecimento dos dados
  - Criação do modelo relacional e joins
- **Saída**: Tabelas relacionais normalizadas prontas para análise

### 3. Silver para Gold (3_silver_to_gold.ipynb)
- **Objetivo**: Criar camada analítica de alto valor para o negócio
- **Processos**:
  - Agregações e cálculos de métricas de negócio
  - Criação de tabelas fato e dimensão (modelo estrela)
  - Preparação de datasets específicos para casos de uso analíticos
  - Otimização para consultas analíticas de alto desempenho
- **Saída**: Modelo dimensional otimizado para análises de negócio

### 4. Análise Exploratória de Dados (4_analise_exploratoria.ipynb)
- **Objetivo**: Entender os padrões e características dos dados
- **Análises**:
  - Volume de pedidos por mês e análise de sazonalidade
  - Distribuição do tempo de entrega e impacto na operação
  - Relação entre frete e distância (proxy por estado)
  - Análise de categorias por faturamento (curva ABC/Pareto)
  - Valor médio de pedido por estado brasileiro
- **Resultados**: Visualizações e insights sobre padrões de vendas e logística

### 5. Solução de Problemas de Negócio (5_solucao_problemas.ipynb)
- **Objetivo**: Resolver questões específicas de negócio com análises avançadas
- **Implementações**:
  - **Análise de Retenção**: Cálculo e análise da taxa de clientes recorrentes
  - **Predição de Atraso**: Modelo de machine learning para prever entregas atrasadas
  - **Segmentação de Clientes**: Clustering para identificar perfis de clientes
  - **Análise de Satisfação**: Exploração dos fatores que impactam a avaliação dos clientes
- **Resultados**: Modelos e recomendações acionáveis para o negócio

### 6. Visualização e Dashboards (6_visualizacao_dashboards.ipynb)
- **Objetivo**: Criar painéis interativos para monitoramento de KPIs
- **Dashboards**:
  - Dashboard de evolução de vendas com filtros dinâmicos por estado e categoria
  - Mapa de calor por região/estado para análise geográfica de vendas
  - Análise da relação entre avaliação do cliente e tempo de entrega
  - Dashboard de desempenho de vendedores (volume, satisfação e tempo de entrega)
- **Resultados**: Painéis interativos para tomada de decisão em tempo real

## Modelo de Dados

O modelo estrela implementado na camada Gold segue esta estrutura:

```mermaid
erDiagram
    DIM_TIME ||--o{ FACT_SALES : references
    DIM_CUSTOMERS ||--o{ FACT_SALES : references
    DIM_PRODUCTS ||--o{ FACT_SALES : references
    DIM_SELLERS ||--o{ FACT_SALES : references
    FACT_SALES ||--o{ FACT_REVIEWS : references
    
    DIM_TIME {
        date date_id PK
        int year
        int quarter
        int month
        string month_name
        int week
        int day
        boolean is_weekend
    }
    
    DIM_CUSTOMERS {
        string customer_id PK
        string customer_city
        string customer_state
        string zip_code_prefix
    }
    
    DIM_PRODUCTS {
        string product_id PK
        string category_name
        string category_name_english
        float weight_g
        float length_cm
        float height_cm
        float width_cm
        float volume_cm3
    }
    
    DIM_SELLERS {
        string seller_id PK
        string seller_city
        string seller_state
        string zip_code_prefix
    }
    
    FACT_SALES {
        string order_id PK
        string customer_id FK
        string seller_id FK
        string product_id FK
        date order_purchase_timestamp FK
        float price
        float freight_value
        date order_delivered_date
        date order_estimated_delivery_date
    }
    
    FACT_REVIEWS {
        string review_id PK
        string order_id FK
        int review_score
        string review_comment_title
        string review_comment_message
        date review_creation_date
        date review_answer_timestamp
    }
```

## Principais Insights de Negócio

As análises realizadas geraram os seguintes insights principais:

1. **Comportamento de Vendas**:
   - Foi identificada sazonalidade nas vendas, com picos em novembro (Black Friday) e datas comemorativas
   - O ticket médio varia significativamente por categoria de produto
   - Há concentração de vendas em poucos estados (SP, RJ, MG)

2. **Logística e Entregas**:
   - Tempo médio de entrega: 12 dias
   - 15% dos pedidos são entregues com atraso
   - Principais fatores de atraso: distância, peso do produto e período de alta demanda

3. **Segmentação de Clientes**:
   - Identificados 4 segmentos principais de clientes com comportamentos distintos
   - Taxa de retenção geral: apenas 3% são clientes recorrentes
   - Estratégias específicas desenvolvidas para cada segmento

4. **Satisfação do Cliente**:
   - Forte correlação entre tempo de entrega e avaliação
   - Categorias com melhor e pior avaliação identificadas
   - Preço não é fator determinante da satisfação, mas sim cumprimento de expectativas de entrega

5. **Oportunidades de Negócio**:
   - Categorias com potencial de crescimento identificadas
   - Estados com baixa penetração mas alto ticket médio representam oportunidade
   - Recomendações para aumentar taxa de retenção de clientes

## Resultados da Solução de Problemas de Negócio

### 1. Análise de Retenção
- Taxa de clientes recorrentes: apenas ~3% dos clientes realizaram mais de uma compra
- A maioria dos clientes (97%) faz apenas uma compra e não retorna
- Recomendações: implementar programa de fidelidade, melhorar comunicação pós-venda e oferecer descontos para compras recorrentes

### 2. Predição de Atraso
- Modelo de Random Forest para prever entregas atrasadas.
- Fatores que influenciam atrasos incluem: peso e volume do produto, valor do frete, razão preço/frete, se cliente e vendedor são do mesmo estado, e o estado do cliente
- O pipeline gera e salva gráficos da importância das features, matrizes de confusão e métricas de avaliação do modelo.
- A implementação permite ações preventivas e gerenciamento de expectativas dos clientes.

### 3. Segmentação de Clientes
- Identificados 4 perfis principais de clientes:
  - **Alto Valor**: Compram menos frequentemente, mas com alto ticket médio
  - **Compradores Frequentes**: Realizaram múltiplas compras de valor médio
  - **Compradores Casuais**: Realizaram poucas compras de valor médio
  - **Baixo Engajamento**: Compraram apenas uma vez com ticket baixo
- Estratégias de marketing personalizadas para cada segmento demonstraram aumento na efetividade de campanhas

### 4. Análise de Satisfação
- Correlação negativa forte entre tempo de entrega e avaliação do cliente (-0.65)
- Clientes com entregas realizadas antes do prazo previsto têm 3x mais probabilidade de dar notas máximas
- Categorias com melhor avaliação: produtos para casa, decoração e brinquedos
- Categorias com pior avaliação: eletrônicos e produtos frágeis

## Dashboards Interativos

### Visualização e Exportação
Os dashboards são gerados automaticamente na pasta `dashboards/` nos formatos:
- **HTML**: Interativo, para navegação no navegador.
- **PNG**: Imagem estática, ideal para relatórios e apresentações.

> **Observação:** Para exportação de imagens, é necessário o pacote `kaleido` (`pip install -U kaleido`).

### Como visualizar
- **HTML**: Abra no navegador para interatividade total.
- **PNG**: Visualize diretamente ou insira em relatórios/presentações.

### Principais Dashboards Gerados

| Imagem (PNG) | Nome do Arquivo | Descrição |
|---|---|---|
| ![Evolução das Vendas](dashboards/sales_evolution_dashboard.png) | sales_evolution_dashboard | Evolução das vendas ao longo do tempo |
| ![Evolução por Categoria](dashboards/sales_evolution_by_category_dashboard.png) | sales_evolution_by_category_dashboard | Evolução das vendas por categoria de produto |
| ![Mapa de Calor](dashboards/sales_heatmap.png) | sales_heatmap | Mapa de calor de vendas por estado |
| ![Correlação entre Estados](dashboards/state_correlation_heatmap.png) | state_correlation_heatmap | Correlação de vendas entre estados |
| ![Ticket Médio por Estado](dashboards/average_ticket_by_state.png) | average_ticket_by_state | Ticket médio por estado |
| ![Tempo de Entrega vs Avaliação](dashboards/delivery_time_vs_review.png) | delivery_time_vs_review | Tempo de entrega vs. avaliação do cliente |
| ![Relação Entrega e Avaliação](dashboards/delivery_review_heatmap.png) | delivery_review_heatmap | Relação entre tempo de entrega e avaliação do cliente |
| ![Impacto do Atraso](dashboards/delay_impact_on_review.png) | delay_impact_on_review | Impacto do atraso na avaliação do cliente |
| ![Correlação Atraso-Avaliação](dashboards/delay_days_vs_review.png) | delay_days_vs_review | Correlação entre dias de atraso e avaliação |
| ![Top Vendedores](dashboards/top_sellers_revenue.png) | top_sellers_revenue | Top 20 vendedores por receita total |
| ![Performance dos Vendedores](dashboards/seller_performance_scatter.png) | seller_performance_scatter | Volume de vendas, avaliação e tempo de entrega |
| ![Tempo de Entrega por Volume](dashboards/delivery_time_by_volume.png) | delivery_time_by_volume | Tempo de entrega por categoria de volume |
| ![Avaliação por Estado do Vendedor](dashboards/review_by_seller_state.png) | review_by_seller_state | Avaliação média por estado do vendedor |
| ![KPIs dos Vendedores](dashboards/seller_performance_kpis.png) | seller_performance_kpis | KPIs agregados dos vendedores |

Cada dashboard possui também versões em HTML e png no mesmo diretório.
