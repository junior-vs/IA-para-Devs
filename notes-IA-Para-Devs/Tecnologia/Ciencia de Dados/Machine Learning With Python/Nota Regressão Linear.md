

# 📚 Regressão Linear

## 🧩 Palavras-chave
- Regressão
- Regressão Linear
- Regressão Simples
- Regressão Múltipla
- Variável Dependente
- Variável Independente
- Inclinação (m)
- Intercepto (b)

## 📝 Anotações
### O que é Regressão?
- É uma técnica para entender como diferentes fatores (variáveis independentes) se relacionam com um resultado contínuo (variável dependente).
- O objetivo principal é fazer previsões com base em dados existentes.
- **Exemplo:** Usar o tamanho do motor e o consumo de combustível de um carro para prever suas emissões de CO2.

### Regressão Linear
- É um tipo de regressão que assume que a relação entre as variáveis pode ser representada por uma linha reta.

#### Equação da Linha
- A relação linear é expressa pela equação: `y = mx + b`
    - **y**: Variável dependente (o que se quer prever).
    - **x**: Variável independente (o fator usado para a previsão).
    - **m**: Inclinação da linha (indica quanto `y` muda para cada unidade de mudança em `x`).
    - **b**: Intercepto (o valor de `y` quando `x` é igual a zero).

#### Interpretação dos Coeficientes
- **Inclinação (m)**: Mostra a mudança na variável dependente para cada unidade de mudança na independente.
    - Uma inclinação positiva indica uma relação direta (ambas as variáveis aumentam juntas).
    - Uma inclinação negativa indica uma relação inversa (uma variável aumenta enquanto a outra diminui).
- **Intercepto (b)**: É o valor da variável dependente quando a variável independente é zero. Em alguns contextos, pode não ter uma interpretação prática direta.

### Diferença entre Regressão Simples e Múltipla
#### Regressão Simples
- Utiliza **uma única** variável independente para prever a variável dependente.
- É mais simples de interpretar.
- **Exemplo:** Prever o preço de uma casa usando apenas seu tamanho (`Preço = m * Tamanho + b`).

#### Regressão Múltipla
- Utiliza **duas ou mais** variáveis independentes para prever a variável dependente.
- Permite uma análise mais complexa e potencialmente mais precisa.
- **Exemplo:** Prever o preço de uma casa usando tamanho, número de quartos e localização (`Preço = m1*Tamanho + m2*Quartos + m3*Localização + b`).

### Exemplo Prático: Previsão do Preço de Casas
1.  **Coleta de Dados**: Reunir informações sobre o tamanho e o preço de várias casas.
2.  **Análise e Aplicação**: Usar um software para aplicar a regressão linear e encontrar a linha que melhor se ajusta aos dados, resultando em uma equação.
    - Exemplo de equação: `Preço = 2.000 * Tamanho + 100.000`
3.  **Realização de Previsões**: Usar a equação para estimar o preço de uma nova casa.
    - Para uma casa de 80 m², a previsão seria: `Preço = 2.000 * 80 + 100.000 = 260.000 USD`.

## 📌 Resumo
A regressão é uma técnica para prever um valor contínuo com base em um ou mais fatores. A regressão linear, um tipo específico, modela essa relação através de uma linha reta, definida pela equação `y = mx + b`. A inclinação (`m`) indica como a variável de resultado (`y`) muda com a variável preditora (`x`), e o intercepto (`b`) é o ponto de partida. Enquanto a regressão simples usa um único preditor, a regressão múltipla utiliza vários, permitindo análises mais abrangentes, como prever o preço de uma casa com base em seu tamanho e número de quartos.

## 📖 Glossário
- **Regressão**: Técnica estatística para entender e prever a relação entre uma variável dependente contínua e uma ou mais variáveis independentes.
- **Regressão Linear**: Modelo que assume uma relação de linha reta entre as variáveis.
- **Regressão Simples**: Modelo de regressão com apenas uma variável independente.
- **Regressão Múltipla**: Modelo de regressão com duas ou mais variáveis independentes.
- **Variável Dependente (y)**: A variável que se deseja prever.
- **Variável Independente (x)**: A variável usada para fazer a previsão.
- **Inclinação (m)**: O coeficiente que mede a variação na variável dependente para cada unidade de mudança na variável independente.
- **Intercepto (b)**: O valor da variável dependente quando a variável independente é zero.

## ❓ Perguntas e Respostas
 
1. **Definição e Conceitos Básicos:**
    - O que é regressão e qual é seu objetivo principal?
    - Como a regressão se relaciona com o aprendizado supervisionado?
2. **Tipos de Regressão:**
    - Quais são as principais diferenças entre regressão simples e múltipla?
    - O que caracteriza a regressão linear e a regressão não linear?
3. **Aplicações da Regressão:**
    - Quais são algumas aplicações práticas da análise de regressão em diferentes setores?
    - Como a regressão pode ser utilizada para prever vendas ou preços de imóveis?
4. **Modelo de Regressão:**
    - O que é um modelo de regressão e como ele é construído?
    - Quais são os componentes de uma equação de regressão?
5. **Interpretação dos Coeficientes:**
    - Como interpretar o coeficiente de uma variável em um modelo de regressão?
    - O que significa o intercepto em uma equação de regressão?
6. **Avaliação do Modelo:**
    - Quais métricas podem ser usadas para avaliar a performance de um modelo de regressão?
    - O que é o coeficiente de determinação (R²) e como ele é interpretado?
7. **Desafios e Considerações:**
    - Quais são algumas suposições que devem ser atendidas em um modelo de regressão?
    - O que pode acontecer se essas suposições não forem atendidas?
8. **Algoritmos de Regressão:**
    - Quais são alguns algoritmos modernos de regressão mencionados no vídeo?
    - Como a regressão de floresta aleatória difere da regressão linear?


