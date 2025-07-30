# **Workflow de Alta Performance: Do Dado Bruto à Análise do Modelo de Classificação**
**(Dataset: Câncer de Mama de Wisconsin)**

## **Etapa 1: Configuração do Ambiente e Compreensão dos Dados**

*   [ ] **1.1. Importar Bibliotecas Fundamentais:** `pandas` para manipulação de dados, `numpy` para operações numéricas, `matplotlib` e `seaborn` para visualização.
*   [ ] **1.2. Carregar o Dataset:** `pd.read_csv('data.csv')`.
*   [ ] **1.3. Inspeção Estrutural Imediata:**
    *   [ ] **Shape (`.shape`):** Entender as dimensões (quantas amostras e features temos?).
    *   [ ] **Tipos de Dados (`.info()`):** Verificar se as colunas estão com os `dtypes` corretos (numéricas como `float64`/`int64`, categóricas como `object`).
    *   [ ] **Visão Geral (`.head()`):** Inspecionar as primeiras linhas para entender a estrutura.
*   [ ] **1.4. Limpeza Preliminar:**
    *   [ ] **Remover Colunas Inúteis:** Identificar e remover colunas que não carregam informação preditiva (`.drop()`).
        *   *Tarefa específica:* Remover as colunas `id` e `Unnamed: 32`.

## **Etapa 2: Análise Exploratória de Dados (EDA) — A Fase de Investigação**

_Objetivo: Gerar insights, identificar padrões, validar hipóteses e informar as decisões de pré-processamento e modelagem. Esta é a etapa mais crítica para o sucesso do modelo._

### **2.1. Análise Univariada (Análise de Variável Única)**
*   [ ] **2.1.1. Análise da Variável Alvo (`diagnosis`):**
    *   [ ] **Tarefa:** Calcular e visualizar (com `countplot`) a distribuição das classes 'M' (Maligno) e 'B' (Benigno).
    *   **Impacto no Modelo:** Identificar se há **desbalanceamento de classes**. Um desbalanceamento severo exigiria o uso de métricas como F1-Score em vez de apenas acurácia, e possivelmente técnicas de reamostragem (oversampling/undersampling).
*   [ ] **2.1.2. Análise da Distribuição das Features Numéricas:**
    *   [ ] **Tarefa:** Gerar **histogramas** para todas as 30 features numéricas para entender a forma de suas distribuições (ex: simétrica, assimétrica à direita/esquerda).
    *   **Impacto no Modelo:** Distribuições muito assimétricas podem ser candidatas a transformações (ex: logarítmica) para melhorar o desempenho de alguns modelos.
*   [ ] **2.1.3. Análise de Outliers:**
    *   [ ] **Tarefa:** Gerar **boxplots** para todas as 30 features para identificar visualmente a presença de outliers.
    *   **Impacto no Modelo:** Outliers podem distorcer o treinamento de modelos sensíveis a eles (como SVM). Esta análise informa a necessidade (ou não) de uma estratégia de tratamento de outliers na Etapa 3.

### **2.2. Análise Bivariada (Análise de Pares de Variáveis)**
*   [ ] **2.2.1. Relação entre Features e a Variável Alvo (Seleção de Features):**
    *   [ ] **Tarefa:** Para cada uma das 30 features, criar um **boxplot ou violin plot** comparando sua distribuição para as classes 'M' e 'B'.
    *   **Impacto no Modelo:** Esta é uma das tarefas mais importantes. Ela permite **identificar visualmente as features mais preditivas**. Features cujas distribuições são muito diferentes entre as classes 'M' e 'B' (pouca sobreposição) são fortes candidatas a serem bons preditores.
*   [ ] **2.2.2. Relação entre Features Numéricas (Análise de Multicolinearidade):**
    *   [ ] **Tarefa:** Calcular a matriz de correlação (`.corr()`) e visualizá-la com um **heatmap** (`seaborn.heatmap`).
    *   **Impacto no Modelo:** Identificar pares ou grupos de features com correlação muito alta (ex: > 0.9). A multicolinearidade pode desestabilizar os coeficientes de modelos lineares (como Regressão Logística) e indica redundância de informação, justificando o uso de PCA.

### **2.3. Análise Multivariada (Análise de Múltiplas Variáveis em Conjunto)**
*   [ ] **2.3.1. Análise de Separabilidade de Classes com PCA:**
    *   [ ] **Tarefa:** Aplicar `StandardScaler` seguido de `PCA(n_components=2)` nos dados. Em seguida, criar um **gráfico de dispersão (scatter plot)** com os dois primeiros Componentes Principais (PC1 vs PC2), colorindo os pontos pela variável `diagnosis`.
    *   **Impacto no Modelo:** Esta é a tarefa que **valida a viabilidade do projeto**. Se as classes 'M' e 'B' formarem clusters visualmente separáveis neste gráfico 2D, isso é um forte indicador de que um modelo de classificação terá sucesso. Se os pontos estiverem completamente misturados, o problema é muito mais difícil.

## **Etapa 3: Pré-Processamento e Engenharia de Features**

_Objetivo: Transformar os dados brutos em um formato otimizado para o treinamento de modelos de Machine Learning, aplicando as decisões tomadas na EDA._

*   [ ] **3.1. Definir Features (X) e Alvo (y):** Separar o DataFrame.
*   [ ] **3.2. Codificação da Variável Alvo:** Converter `diagnosis` para numérico (M=1, B=0).
*   [ ] **3.3. Divisão em Treino e Teste:**
    *   [ ] **Tarefa:** Usar `train_test_split` para dividir X e y.
    *   **Impacto no Modelo:** Usar `stratify=y` para garantir que a proporção de classes 'M' e 'B' seja a mesma nos conjuntos de treino e teste. Isso é crucial para uma avaliação justa, especialmente com dados desbalanceados.
*   [ ] **3.4. Escalonamento de Features:**
    *   [ ] **Tarefa:** Inicializar `StandardScaler`, treiná-lo (`.fit()`) **apenas com `X_train`** e aplicá-lo (`.transform()`) em `X_train` e `X_test` para evitar vazamento de dados.
*   [ ] **3.5. Redução de Dimensionalidade (PCA para Modelagem):**
    *   [ ] **Tarefa:** Inicializar e treinar o PCA (`.fit()`) **apenas nos dados de treino escalonados**. Aplicar a transformação (`.transform()`) em ambos os conjuntos.
    *   **Impacto no Modelo:** Cria um novo conjunto de dados (ex: `X_train_pca`, `X_test_pca`) para treinar um modelo mais simples e potencialmente mais rápido, livre de multicolinearidade.

## **Etapa 4: Modelagem e Treinamento**

* [ ] **4.1. Seleção e Comparação de Múltiplos Modelos:**     
    -  [ ] **Tarefa:** Escolher de 3 a 4 algoritmos de classificação de famílias diferentes.       
    - **Sugestões:**       
        - `LogisticRegression` (Baseline linear e interpretável).            
        - `KNeighborsClassifier` (Baseado em distância).            
        - `SVC` (Máquina de Vetores de Suporte).            
        - `RandomForestClassifier` (Baseado em árvores, geralmente de alta performance).            
- [ ] **4.2. Treinamento e Avaliação Inicial (com Validação Cruzada):**    
    - [ ] **Tarefa:** Para cada modelo, usar `cross_val_score`nos dados de treino para obter uma estimativa robusta do seu desempenho antes da otimização. Avaliar com a métrica recall.        
- [ ] **4.3. Otimização de Hiper-parâmetros:**    
    - [ ] **Tarefa:** Para o(s) melhor(es) modelo(s) da etapa anterior, usar `GridSearchCV` para encontrar a melhor combinação de hiper-parâmetros.        
    - **Exemplo:** O `GridSearchCV` pode testar diferentes valores de C para a Regressão Logística, diferentes `n_neighbors` para o KNN, e diferentes `n_components` para o PCA, tudo de forma integrada com a pipeline.
        
- [ ] **4.4. Treinamento do Modelo Final:**
    
    - **Tarefa:** Treinar o melhor modelo, com os melhores hiperparâmetros encontrados pelo GridSearchCV, usando o conjunto de treino completo.

## **Etapa 5: Avaliação Pós-Modelo e Análise de Desempenho**

_Objetivo: Ir além de uma única métrica (acurácia) para entender *como* e *onde* o modelo acerta e erra._

*   [ ] **5.1. Fazer Previsões:**
    *   [ ] **Tarefa:** Usar os modelos treinados para fazer previsões no conjunto de teste (`.predict(X_test_scaled)` e `.predict(X_test_pca)`).
*   [ ] **5.2. Calcular Métricas de Classificação:**
    *   [ ] **Tarefa:** Para ambos os modelos, calcular: Acurácia, Precisão, Recall, F1-Score e a Área Sob a Curva ROC (AUC).
    *   **Impacto no Modelo:** A análise conjunta dessas métricas dá uma visão completa. Em um problema médico, o **Recall** (taxa de verdadeiros positivos) é frequentemente a métrica mais importante (queremos minimizar os falsos negativos – pacientes com câncer diagnosticados como saudáveis).
*   [ ] **5.3. Análise da Matriz de Confusão:**
    *   [ ] **Tarefa:** Gerar e visualizar a matriz de confusão para ambos os modelos.
    *   **Impacto no Modelo:** Esta é uma análise de erro fundamental. Permite quantificar e interpretar os tipos de erro que o modelo comete:
        *   **Falsos Positivos (FP):** Pacientes saudáveis diagnosticados com câncer.
        *   **Falsos Negativos (FN):** Pacientes com câncer diagnosticados como saudáveis (o erro mais perigoso neste contexto).
	- [ ]**5.4. Interpretabilidade do Modelo:**    
	    - [ ] **Tarefa:** Extrair e visualizar a importância das features.        
		    - **Métodos:**        
	        - Para modelos lineares: model.coef_.           
	        - Para modelos de árvore: model.feature_importances_.            
	        - **(Avançado/Bônus):** Usar a biblioteca shap para explicar previsões individuais, como solicitado no desafio.            
	- [ ]**5.5. Análise Crítica e Implicações Práticas:**    
	    - [ ] **Tarefa:** Responder às perguntas-chave do desafio.        
	        - O desempenho do modelo (especialmente o Recall) é aceitável para uso clínico como ferramenta de apoio?            
	        - Qual o custo de um Falso Negativo neste cenário?            
	        - Como a interpretabilidade do modelo pode ajudar o médico a confiar (ou não) na sugestão da IA?

## **Etapa 6: Conclusão Final e Próximos Passos**

*   [ ] **6.1. Documentar Resultados:** Sumarizar qual modelo (completo ou PCA) teve o melhor desempenho balanceado, com foco na métrica de negócio mais importante (Recall).
*   [ ] **6.2. Propor Melhorias:** Sugerir próximos passos, como:
    *   Testar algoritmos mais complexos (ex: `RandomForest`, `XGBoost`).
    *   Realizar otimização de hiperparâmetros (`GridSearchCV`).
    *   Investigar os erros do modelo (os Falsos Negativos) para entender se há algum padrão neles.