Aqui está a lista de conceitos aprendidos:

### 1. Fundamentos da Estatística e Tipos de Dados
*   **Classificação de Variáveis**: A distinção fundamental entre diferentes tipos de dados.
    *   **Variáveis Qualitativas (Categóricas)**: Representam características ou qualidades.
        *   **Nominais**: Categorias sem ordem intrínseca (ex: `categoria_produto`, `regiao_cliente`).
        *   **Ordinais**: Categorias com uma ordem ou hierarquia definida (ex: `avaliacao` do produto, transformada de 1-5 para "Péssimo" a "Ótimo").
    *   **Variáveis Quantitativas (Numéricas)**: Representam valores mensuráveis.
        *   **Discretas**: Valores inteiros e contáveis (ex: `quantidade` de produtos).
        *   **Contínuas**: Valores que podem assumir qualquer número em um intervalo (ex: `total_compra`).

### 2. Análise de Frequência (Estatística Descritiva)
*   **Distribuição de Frequência para uma variável**: Como organizar e resumir os dados para entender a ocorrência de cada categoria.
    *   **Frequência Absoluta**: A contagem de quantas vezes cada valor aparece.
    *   **Frequência Relativa (e Percentual)**: A proporção de cada valor em relação ao total.
*   **Distribuição de Frequência para duas variáveis**: Análise do relacionamento entre duas variáveis categóricas.
    *   **Tabela de Contingência (ou Tabela Cruzada)**: Usada para visualizar a frequência conjunta de duas variáveis (ex: avaliação por região).
    *   **Tabela Cruzada com Agregação**: Cálculo de uma medida estatística (como a média do `total_compra`) para o cruzamento de duas categorias.

### 3. Medidas de Tendência Central
*   **Média**: O valor médio de um conjunto de dados, sensível a valores extremos.
*   **Mediana**: O valor central que divide o conjunto de dados ao meio, mais robusto a outliers.
*   **Moda**: O valor que aparece com maior frequência.
    *   Conceito de **Bimodalidade/Multimodalidade** (quando há mais de uma moda).
*   **Relação entre Média, Mediana e Moda**: Como a posição relativa dessas três medidas ajuda a entender a **simetria** ou **assimetria** de uma distribuição de dados.

### 4. Medidas Separatrizes (Medidas de Posição)
*   **Quartis (Q1, Q2, Q3)**: Valores que dividem os dados em quatro partes iguais.
*   **Percentis**: Valores que dividem os dados em cem partes iguais, úteis para identificar "top X%" (ex: 1% maiores salários ou 20% colaboradores mais jovens).

### 5. Medidas de Dispersão (Variabilidade)
*   **Desvio Médio Absoluto (MAD)**: A média do desvio absoluto de cada ponto em relação à média do conjunto.
*   **Variância**: Medida de quão dispersos os dados estão em relação à média (ao quadrado).
*   **Desvio Padrão**: A raiz quadrada da variância, retornando a medida para a unidade original dos dados e sendo mais interpretável.

### 6. Visualização de Dados Estatísticos
*   **Gráfico de Barras**: Para visualizar a frequência de variáveis categóricas.
*   **Histograma**: Para visualizar a distribuição de frequência de dados quantitativos.
    *   **Regra de Sturges**: Método para determinar o número ideal de classes (bins) em um histograma.
    *   **Curva de Densidade (KDE)**: Para estimar e visualizar a forma da distribuição.
*   **Boxplot**: Representação gráfica que resume a distribuição de dados através de quartis, mediana e identificação de **outliers**.
*   **Gráfico de Violino**: Combina um boxplot com uma curva de densidade para mostrar a distribuição dos dados.

Essa é uma excelente base de estatística descritiva, fundamental para qualquer análise de dados e para a construção de modelos de IA. Se quiser aprofundar em algum desses tópicos, é só pedir