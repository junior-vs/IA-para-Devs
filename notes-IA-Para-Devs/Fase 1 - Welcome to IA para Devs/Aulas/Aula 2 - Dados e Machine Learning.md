## Resumo:

A Aula 2 de Fundamentos de Inteligência Artificial focou no Machine Learning, explicando como os computadores aprendem com dados para tomar decisões inteligentes sem programação explícita1. A aula demonstrou a importância da ética na IA com o caso da Target, que previu a gravidez de uma adolescente, e o caso da mineração de dados em supermercados, que associou fraldas a cervejas.

Foi apresentada uma demonstração prática em Python usando a biblioteca Scikit-learn, treinando um modelo para prever a solubilidade de compostos químicos na água A aula explicou a importância da preparação dos dados (limpeza, transformação e normalização) e como avaliar a precisão do modelo usando o _accuracy score_.

Os três tipos de aprendizado em Machine Learning foram detalhados: supervisionado (com dados rotulados, como identificar frutas), não supervisionado (encontrar padrões em dados não rotulados, como agrupar frutas por cor), e por reforço (aprender por tentativa e erro, como em um jogo de videogame). Foram citados modelos comuns de Machine Learning, como Classificador de Naive Bayes, K-NN, Regressão Linear, Árvore de Decisão e Modelagem por Agrupamento.

A aula também abordou os tipos de dados (estruturados, semi-estruturados, não-estruturados e temporais) e a importância de analisá-los corretamente para evitar "alucinações" (previsões incorretas). O processo de treinamento do modelo envolve coleta, limpeza, transformação e ajuste dos dados.

## Conceitos:

1. **Machine Learning (Aprendizado de Máquina)**: Tecnologia que permite aos computadores aprender diretamente dos dados, tomando decisões inteligentes sem serem explicitamente programados para cada situação. Quanto mais dados inseridos, mais precisa será a análise13.
    
2. **Ética na IA**: A importância de considerar os aspectos éticos ao trabalhar com Machine Learning e dados, como demonstrado no caso da Target, onde a previsão de gravidez levantou questões de privacidade141414141414.
    
3. **Preparação de Dados**: Etapa crucial no Machine Learning que envolve limpar (remover informações inúteis), transformar (padronizar) e normalizar os dados para que a máquina consiga identificá-los e fazer uma análise melhor15.
    
4. **Scikit-learn**: Uma biblioteca Python muito utilizada em Machine Learning e outras aplicações de inteligência artificial16.
    
5. **Accuracy Score (Pontuação de Precisão)**: Ferramenta utilizada para testar a taxa de acerto de um modelo de Machine Learning, comparando as previsões do modelo com as respostas corretas17.
    
6. **Aprendizado Supervisionado**: Tipo de aprendizado de máquina onde o modelo é treinado com dados rotulados, ou seja, com as respostas corretas fornecidas. É comparado a ensinar alguém o que são frutas mostrando e nomeando cada uma18.
    
7. **Aprendizado Não Supervisionado**: Tipo de aprendizado de máquina onde o modelo encontra padrões e estruturas em dados não rotulados, sem ter as respostas corretas fornecidas. É como dar um monte de frutas a alguém e pedir para que as separe por características19.
    
8. **Aprendizado por Reforço**: Tipo de aprendizado de máquina onde o modelo aprende por tentativa e erro, sendo "recompensado" por ações corretas e "punido" por ações incorretas, similar a um jogo de videogame20.
    
9. **Modelos de Machine Learning**: Diferentes algoritmos e abordagens para o aprendizado de máquina, incluindo:
    - **Classificador de Naive Bayes**: Utiliza a teoria da probabilidade para classificar dados21.
        
    - **K-NN (K-Nearest Neighbor)**: Classifica dados com base na proximidade de exemplos conhecidos22.
        
    - **Regressão Linear**: Aplica uma relação linear entre variáveis para prever valores contínuos23.
        
    - **Árvore de Decisão**: Usa uma estrutura de "se-então" para tomar decisões24.
        
    - **Modelagem por Agrupamento**: Identifica agrupamentos de dados com base em similaridades, muito usada em marketing para segmentação de clientes.
        
10. **Tipos de Dados**:
    - **Estruturados**: 
	    - Dados bem organizados, geralmente em tabelas, fáceis de trabalha.
	    - Dados estruturados são aqueles organizados de maneira clara e lógica, geralmente me tabelas com linhas e colunas. Esses dados seguem um modelo que define o seu formato, como um bando de dados relacional.
	    - Eles são facilmente identificáveis por sua organização em tabelas, onde cada linha representa um registro e cada coluna um atributo deses registro. por exemplo, imagine um banco de dados de uma biblioteca, conde cada livro tem um Id, titulo, autor, e ano de publicação.
        
    - **Não-estruturados**: 
	    - Dados que podem vir de diversas fontes (e-mail, vídeo), exigindo modelos mais complexos para extração de informações
	    - Danos não estruturados são informações que nao seguem um modelo ou formato especifico. Eles são mais complexos para processar e analisar porque não tem uma estrutura definida. 
	    - Eles podem ser identificados pela ausência de um formato regular e consistente
	    - exemplos: textos livres, imagens, videos, audios. 
        
    - **Semi-estruturados**: 
	    - Não estão em tabelas, mas possuem alguma organização, como o formato JSON
	    - Nao se encaixam em tabelas, mas ainda possuem algum nível de organização, como tag ou marcadores.
	    - podemos reconhe-los pela presença de aluns elementes de estrutura que facilitam a identificação de diferentes partes dos dados. 
	    - XML, JSON, 
        
    - **Temporais**: 
	    - Dados coletados ao longo do tempo, como vendas anuais.
	    - Séries de Dados Temporais são conjuntos de pontos de dados coletados em intervalos regulares ao longo do tempo. Esses dados são valiosos para analisar
	    - Os dados são organizados sequencialmente em função do tempo. Cada ponto de dados tem um carimbo de tempo associado, indicando quando foi coletado. 
        
11. **Alucinações (em Machine Learning)**: Previsões incorretas ou irrelevantes do modelo, geralmente causadas por dados mal treinados ou não suficientemente limpos
12. . Os V's do Big Data
	1. Volume: Refere-se à quantidade imensa de dados que são gerados atualmente. Com a evolução da tecnologia digital, a geração de dados — provenientes de transações online, mídias sociais, dispositivos IoT, entre outras fontes — cresceu exponencialmente.
	2. Velocidade: Diz respeito à rapidez com que os dados são gerados e processados24. Em um mundo conectado, os dados fluem a uma taxa incrível, e a velocidade com que precisam ser processados é crucial
	3. Variedade: Indica a diversidade dos tipos de dados. Diferente do passado, onde a maioria dos dados era estruturada e facilmente organizada em tabelas, hoje os dados aparecem em diversas formas, incluindo dados estruturados (em bancos de dados tradicionais), dados não estruturados (como textos, vídeos e imagens) e dados semiestruturados (que possuem alguma organização como tags ou marcadores)4
	4. Veracidade: Relaciona-se à qualidade e precisão dos dados. Com a enorme quantidade de dados gerados, garantir que sejam precisos e confiáveis é vital, pois dados imprecisos podem levar a conclusões e decisões equivocadas.
	5. Valor: Considerado por uma das fontes como talvez o "V" mais importante7, refere-se à capacidade de transformar os dados brutos em insights valiosos28. Ter acesso a grandes volumes de dados rápidos e variados não é suficiente se esses dados não forem analisados para extrair informações que possam ser usadas para melhorar processos de negócios, decisões de clientes e estratégias de mercado8.

###  CRISP-DM (Cross-Industry Standard Process for Data Mining).

O **CRISP-DM** é apresentado como um **modelo de processo robusto e amplamente utilizado para projetos de mineração de dados e análise preditiva**. Ele organiza o trabalho em **seis fases distintas**, que guiam a equipe através do ciclo de vida de um projeto de análise de dados.

Aqui estão as seis fases do CRISP-DM detalhadas:

1. **Entendimento do Negócio (Business Understanding)**: Esta é a fase inicial. O foco está em **compreender os objetivos e requisitos do projeto do ponto de vista do negócio**. Esse conhecimento é então transformado em uma **definição clara do problema de mineração de dados** e em um **plano preliminar** para alcançar os objetivos estabelecidos.
2. **Entendimento dos Dados (Data Understanding)**: Nesta fase, ocorre a **coleta inicial dos dados** e a familiarização com eles. O trabalho envolve identificar **problemas de qualidade dos dados** e descobrir os **primeiros insights** contidos neles.
3. **Preparação dos Dados (Data Preparation)**: Esta é a fase onde os dados são efetivamente **limpos e transformados**. As tarefas incluem a **seleção de tabelas, registros e atributos relevantes**, além de **transformar e limpar os dados** para que estejam prontos para a modelagem. Uma parte essencial desta fase é a limpeza de dados, que pode envolver garantir consistência, remover duplicatas, tratar dados discrepantes (outliers), aplicar regras de validação, organizar dados para armazenamento eficiente, remover dados triviais, fundir dados de diferentes fontes, usar codificação One-Hot para variáveis categóricas e aplicar tabelas de conversão.
4. **Modelagem (Modeling)**: Aqui, as **técnicas de modelagem são selecionadas e aplicadas** para construir diversos modelos. Esta fase requer o uso de métodos de seleção de dados e, frequentemente, a criação de vários modelos para, em seguida, escolher o mais adequado ao problema. Exemplos de algoritmos de machine learning que podem ser utilizados nesta fase incluem Classificador Naive Bayes, K-Nearest Neighbor (K-nn), Regressão Linear, Árvore de Decisão e Modelagem por Agrupamento (Clustering).
5. **Avaliação (Evaluation)**: Nesta fase crucial, os **modelos construídos são avaliados** com base nos critérios de sucesso definidos no início do projeto. O objetivo é **garantir que os passos executados para construir o modelo realmente atendam aos objetivos do negócio**.
6. **Implantação (Deployment)**: Esta é a fase final do processo. O modelo avaliado e aprovado é **aplicado para resolver o problema de negócio**. A forma de implantação pode variar bastante, desde a simples geração de um relatório até a implementação de um processo iterativo de tomada de decisão que afete toda a organização.

A fonte fornece um **exemplo prático** de como o CRISP-DM se aplica a um projeto de **previsão de demanda em varejo**:

- **Entendimento do Negócio**: Uma cadeia de supermercados quer otimizar o estoque prevendo a demanda para evitar falta ou excesso de produtos.
- **Entendimento dos Dados**: Coleta de dados históricos de vendas, promoções, sazonalidade e dados econômicos. Observação de padrões sazonais e influência de feriados.
- **Preparação dos Dados**: Limpeza de dados incompletos/errados, transformação de variáveis (como datas) e integração de dados de feriados e promoções.
- **Modelagem**: Teste de modelos como regressão linear, árvores de decisão e redes neurais, treinando-os com dados históricos.
- **Avaliação**: Comparação dos modelos pela precisão da previsão, escolhendo o que melhor equilibra precisão e simplicidade para uso operacional (neste caso, uma rede neural é identificada como a mais precisa).
- **Implantação**: O modelo escolhido é integrado ao sistema de planejamento de estoque, prevendo a demanda semanal por produto para orientar compras e armazenamento.

Este exemplo demonstra como o CRISP-DM permite uma abordagem sistemática e orientada por dados para resolver problemas de negócio complexos, levando à otimização do inventário, redução de custos e melhoria da satisfação do cliente.

### Machine Learning

O Machine Learning é apresentado como uma **área central da Inteligência Artificial (IA)**, sendo, na verdade, um **subconjunto da IA**. Ele é definido como um **conjunto de técnicas e algoritmos** que se assemelham ao processo natural de aprendizagem em seres vivos. A ideia principal é que, assim como organismos biológicos aprimoram habilidades a partir de experiências, os algoritmos de Machine Learning "aprendem" a realizar tarefas analisando e interpretando dados. É importante notar, no entanto, que as máquinas não "aprendem" no sentido humano; elas armazenam e computam, utilizando antropomorfismos para transmitir mecanismos matemáticos complexos.

No coração do Machine Learning está a capacidade de **computar fórmulas a partir de dados para criar "modelos"** que operam como programas. Isso é diferente dos métodos de programação tradicionais, onde as regras são explicitamente codificadas. Enquanto métodos tradicionais de ML frequentemente envolvem etapas sequenciais como pré-processamento, extração e seleção manual de características, seguidas pelo aprendizado e classificação, o Machine Learning, especialmente o Deep Learning, tem a capacidade de **automatizar a aprendizagem de conjuntos de características**.

A eficácia de um algoritmo de Machine Learning depende muito da **integridade da representação dos dados de entrada**. Uma boa representação de dados fornece um desempenho melhor em comparação com uma representação ruim. A importância dos dados para a IA, e consequentemente para o Machine Learning, é destacada, sendo os **dados a "força vital" que alimentam os algoritmos** e moldam o futuro da tecnologia. O crescimento exponencial do **Big Data** contribuiu para a popularidade do Deep Learning, um tipo de algoritmo de Machine Learning.

O processo de criação de um serviço de Machine Learning pode ser comparado ao treinamento de um novo funcionário, envolvendo várias etapas:
1.  **Ordenação dos Dados**: Organizar e preparar os dados que o computador usará para aprender, removendo informações desnecessárias ou confusas.
2.  **Escolha do Modelo**: Selecionar um modelo ou método de ensino específico, pois alguns modelos são melhores para tarefas específicas (como identificar padrões ou prever eventos futuros).
3.  **Treinamento do Modelo**: Usar os dados preparados para ensinar o computador a analisar, encontrar padrões e regras, e aprender a realizar a tarefa desejada.
4.  **Avaliação do Modelo**: Testar o modelo usando dados nunca vistos antes para verificar quão bem ele realiza a tarefa e se pode aplicar o que aprendeu a novas situações.
5.  **Sintonia Fina do Modelo**: Ajustar o modelo com base nos resultados dos testes para melhorar seu desempenho, mudando como ele interpreta os dados, adicionando mais exemplos ou ajustando as "regras" usadas para tomar decisões.

O Machine Learning abrange diferentes **tipos de aprendizagem**:
*   **Aprendizado Supervisionado**: O computador é treinado com **dados rotulados** (entrada e saída desejada), aprendendo a fazer previsões ou tomar decisões corretas em dados novos, mas semelhantes. É como um professor ensinando com exemplos resolvidos. É amplamente usado em diversas áreas como saúde, finanças, reconhecimento de voz e marketing.
*   **Aprendizado Não Supervisionado**: O sistema aprende e identifica padrões em **dados sem rótulos ou orientação externa**. O algoritmo trabalha com informações "cruas" para descobrir estruturas ou relações ocultas. É como deixar uma criança organizar brinquedos sem instruções. Aplicações incluem segmentação de clientes, detecção de anomalias e organização de grandes conjuntos de dados.
*   **Aprendizagem por Reforço (ou Deep Reinforcement Learning no contexto de DL)**: O sistema aprende a tomar decisões através de **tentativa e erro**, recebendo recompensas por ações corretas e, às vezes, penalidades por incorretas. É útil em situações com regras complexas ou desconhecidas. É aplicado em jogos, robótica, sistemas de recomendação e otimização de processos.
*   **Aprendizado Semissupervisionado**: Utiliza um grande conjunto de dados onde **apenas parte é rotulada**. É um meio-termo entre o supervisionado e o não supervisionado. É valioso quando obter dados rotulados é difícil ou caro, mas dados não rotulados são abundantes. Aplicações incluem classificação de textos, análise de sentimentos, detecção de fraude e reconhecimento de imagens.

As fontes mencionam vários **algoritmos de Machine Learning** importantes, muitos deles utilizados na fase de Modelagem do processo CRISP-DM, que discutimos anteriormente:
*   **Classificador Naive Bayes**: Baseado no Teorema de Bayes, assume independência ingênua entre os atributos. É rápido e fácil de implementar.
*   **K-Nearest Neighbor (K-nn)**: Classifica novos pontos com base na maioria da classe dos seus 'K' vizinhos mais próximos. É simples e eficaz, não fazendo suposições sobre a forma dos dados.
*   **Regressão Linear**: Encontra a melhor linha reta para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. Simples e com interpretação clara.
*   **Árvore de Decisão**: Divide os dados em conjuntos menores com base em critérios, formando uma estrutura de árvore onde as decisões são tomadas do nó raiz às folhas. É interpretável.
*   **Modelagem por Agrupamento (Clustering)**: Técnicas não supervisionadas para dividir dados em grupos (clusters) com base em sua similaridade. Inclui algoritmos como K-means.

O Machine Learning, em particular o **Deep Learning (DL)**, tornou-se o "Padrão Ouro" na comunidade de ML e é a abordagem computacional mais utilizada. O DL é altamente escalável e tem demonstrado desempenho notável, superando o desempenho humano em algumas tarefas como classificação de imagens. No entanto, o uso de ML, especialmente modelos profundos, enfrenta desafios como a necessidade de grandes volumes de dados, a gestão de dados desbalanceados, a interpretabilidade dos modelos, o overfitting e problemas de gradiente (vanishing/exploding). Técnicas como Transfer Learning e Data Augmentation são abordagens para lidar com a limitação de dados.

Em resumo, Machine Learning é uma disciplina fundamental da IA que permite que sistemas aprendam com dados para realizar tarefas e criar modelos preditivos ou descritivos. Compreende vários tipos de aprendizagem e algoritmos, sendo o Deep Learning uma subárea proeminente e de grande impacto atualmente.

### Algoritmos de estatística comuns

Este trecho foca em apresentar algumas das **ferramentas estatísticas e matemáticas fundamentais** que são cruciais no contexto do Machine Learning (Aprendizado de Máquina), especialmente para o **entendimento profundo do conjunto de dados** antes de aplicar algoritmos de modelagem. Esses conceitos ajudam a extrair informações valiosas e preparar os dados de forma eficaz.

Os algoritmos e conceitos detalhados na seção são:

1.  **[[Desvio Padrão]]**
    *   **O que é:** É uma **medida de dispersão**. Ele indica **o quanto os valores de um conjunto de dados variam em relação à média**.
    *   **Importância no ML:** É **fundamental para avaliar a consistência** dos dados e **detectar anomalias (outliers)**.
    *   **Como funciona/aplica:** Para calcular, primeiro encontra-se a média dos dados. Depois, calcula-se a diferença entre cada valor e a média, eleva-se essas diferenças ao quadrado, faz-se a média desses quadrados e, por fim, tira-se a raiz quadrada do resultado. Um exemplo dado é o conjunto de dados 2, 4, 4, 4, 5, 5, 7, 9, onde o desvio padrão ajuda a entender quão dispersos estão esses números.


2.  **[[Distribuição Normal]]**
    *   **O que é:** Também conhecida como Gaussiana, é uma **distribuição de probabilidade** que descreve **como os valores de um conjunto de dados tendem a se agrupar em torno da média**.
    *   **Importância no ML:** Ajuda a **compreender a distribuição dos dados**, indicando a **probabilidade de ocorrência de diferentes valores** e facilitando a **identificação de padrões e outliers**.
    *   **Como funciona/aplica:** Para verificar se os dados seguem uma distribuição normal, calcula-se a média e o desvio padrão e observa-se a distribuição dos dados em relação à curva normal. O exemplo dado é de notas de alunos que variam simetricamente em torno da média.

3.  **[[Teorema de Bayes]]**
    *   **O que é:** É um **método de cálculo de probabilidades condicionais**. Ele relaciona a **probabilidade de um evento com a ocorrência de outro evento relacionado**. Este teorema é a base para o **Classificador Naive Bayes**, que faz uma suposição "ingênua" de que os atributos são **independentes uns dos outros, dada a classe do resultado**.
    *   **Importância no ML:** É **vital para inferências e previsões em ambientes incertos**. No Classificador Naive Bayes, ele é usado para calcular a probabilidade de um evento com base no **conhecimento prévio**.
    *   **Como funciona/aplica:** Aplica-se identificando as probabilidades conhecidas e utilizando a fórmula 
    $$P(A|B) = \[P(B|A) * P(A)\] / P(B). $$
    * Um exemplo é o diagnóstico médico, calculando a probabilidade de uma doença dada a presença de sintomas. Outro exemplo é classificar e-mails como spam ou não spam com base na frequência de palavras-chave.

4.  **[[Correlação]]**
    *   **O que é:** É uma **medida que descreve o grau de relação entre duas variáveis**.
    *   **Importância no ML:** Ao revelar a **força e a direção da relação** entre variáveis, permite **identificar dependências e potenciais causalidades**.
    *   **Como funciona/aplica:** Usa-se a fórmula do coeficiente de correlação de Pearson. O exemplo prático menciona analisar a relação entre horas de estudo e notas dos alunos.

5.  **[[Extração de Recursos (Feature Extraction)]]**
    *   **O que é:** O processo de **identificar e selecionar um conjunto de características relevantes de um conjunto de dados para facilitar a análise**. É também descrito como a criação de características a partir de dados brutos. Algoritmos de Machine Learning, especialmente Deep Learning, têm a **capacidade de automatizar a aprendizagem de conjuntos de características** sem grande esforço humano.
    *   **Importância no ML:** É **crucial para reduzir a complexidade dos dados**, **selecionando ou transformando variáveis** para **melhor representar e processar a informação relevante**. A **eficácia** de um algoritmo de ML depende muito da **integridade da representação dos dados de entrada**.
    *   **Como funciona/aplica:** Envolve técnicas como **análise de componentes principais (PCA)** ou **seleção de características baseada em estatísticas**. Um exemplo é na análise de imagens, identificando padrões ou cores informativos para classificação. As arquiteturas multi-camadas do Deep Learning extraem características de baixo nível nas camadas iniciais e de alto nível nas camadas finais.

Conectando com nossa conversa anterior sobre o CRISP-DM e Machine Learning, esses "algoritmos de estatística comuns" são ferramentas amplamente utilizadas nas fases iniciais de um projeto de análise de dados:

*   São essenciais na fase de **Entendimento dos Dados (Data Understanding)** para explorar, visualizar e entender as características dos dados, identificar padrões e problemas.
*   Desempenham um papel crucial na fase de **Preparação dos Dados (Data Preparation)**, especialmente para a limpeza, transformação e, notavelmente, para a **Extração de Recursos**, onde os dados são preparados para a modelagem.
*   O Teorema de Bayes é a base de um algoritmo específico (Naive Bayes), que é aplicado na fase de **Modelagem (Modeling)**.

Portanto, esses conceitos estatísticos fornecem a base matemática e as ferramentas necessárias para entender, preparar e, em alguns casos, modelar os dados em um projeto de Machine Learning, seguindo um processo como o CRISP-DM.

# Resumo da Aula 2: Dados e Machine Learning

A Aula 2 se concentra na importância dos dados para a Inteligência Artificial (IA) e em como o Machine Learning (ML) utiliza esses dados para aprender e resolver problemas complexos. Os dados são apresentados como a **"força vital que alimentam os algoritmos"** de IA.

A aula explora o conceito de **Big Data**, definido como o imenso volume de dados, estruturados e não estruturados, que as empresas lidam diariamente. A importância do Big Data reside não apenas na quantidade, mas no que as organizações fazem com ele, analisando-o para obter insights que levam a melhores decisões e estratégias de negócios. 

A aula também aborda diferentes **tipos de dados** cruciais em IA:

- **Dados Estruturados**: organizados de forma clara e lógica, geralmente em tabelas (linhas e colunas), seguindo um modelo definido. Exemplos incluem planilhas de vendas ou bancos de dados de clientes.
- **Dados Não Estruturados**: informações sem um modelo ou formato específico, sendo mais complexas de processar. Exemplos são postagens em mídias sociais, relatórios de texto livre, imagens, vídeos e áudios.
- **Dados Semi Estruturados**: meio-termo com algum nível de organização, como tags ou marcadores, mas sem tabelas rígidas. Exemplos incluem e-mails, arquivos JSON ou documentos HTML.
- **Séries de Dados Temporais**: pontos de dados coletados em intervalos regulares ao longo do tempo, valiosos para analisar tendências e fazer previsões. Exemplos são medidas meteorológicas, cotações de ações ou monitoramento de tráfego.

São introduzidas figuras importantes no campo do Big Data, como **Doug Cutting**, criador do Lucene (um motor de busca de texto de código aberto) e um dos principais desenvolvedores do Apache Hadoop (um framework para processamento distribuído de Big Data). O Hadoop funciona com dois componentes principais: Hadoop Distributed File System (HDFS) para armazenamento distribuído e MapReduce para processamento distribuído.

O **Processo de Dados** é abordado através do modelo **CRISP-DM (Cross-Industry Standard Process for Data Mining)**, um modelo robusto de seis fases para projetos de mineração de dados e análise preditiva: Entendimento do Negócio, Entendimento dos Dados, Preparação dos Dados, Modelagem, Avaliação e Implantação. A **Limpeza de Dados** é um processo essencial na Preparação dos Dados, envolvendo passos como consistência, deduplicação, tratamento de dados discrepantes, regras de validação, armazenamento, trivialidade, fusão, codificação One-Hot e tabela de conversão.

O Machine Learning é o coração da IA e é comparado ao **processo natural de aprendizagem em seres vivos**, onde algoritmos aprimoram habilidades a partir de experiências. Redes neurais artificiais são inspiradas na estrutura do cérebro humano.

Diversos **algoritmos de estatística comuns** são fundamentais para entender conjuntos de dados no ML: Desvio Padrão (variabilidade), Distribuição Normal (agrupamento em torno da média), Teorema de Bayes (probabilidades condicionais), Correlação (relação entre variáveis) e Extração de Recursos (selecionar características relevantes).

O **treinamento de modelos de ML** é descrito como um processo com etapas definidas: Ordenação dos Dados, Escolha do Modelo, Treinamento do Modelo, Avaliação do Modelo e Sintonia Fina do Modelo. Este processo iterativo visa garantir que o computador aprenda e execute a tarefa designada de forma eficaz e precisa.

São apresentados diferentes **tipos de aprendizagem** em Machine Learning:

- **Aprendizado Supervisionado**: treinado com dados rotulados (entrada e saída desejada) para fazer previsões em novos dados. Amplamente utilizado em identificação de doenças, avaliação de crédito, reconhecimento de voz e análise de sentimento.
- **Aprendizado Não Supervisionado**: aprende padrões e organiza dados sem orientação externa ou rótulos. Usado para explorar dados e descobrir padrões ocultos, como segmentação de clientes, detecção de anomalias e organização de dados.
- **Aprendizagem por Reforço**: aprende por tentativa e erro, recebendo recompensas por ações corretas. Útil em situações com regras complexas ou desconhecidas, como jogos, robótica, sistemas de recomendação e otimização de processos.
- **Aprendizado Semissupervisionado**: utiliza um grande conjunto de dados, parte rotulada e parte não. Valioso quando a obtenção de dados rotulados é difícil ou cara, aplicado em classificação de textos, análise de sentimentos, detecção de fraude e reconhecimento de imagens.

A aula detalha alguns **algoritmos principais**:

- **Classificador Naive Bayes**: baseado no Teorema de Bayes, assume independência de atributos. Rápido, fácil de implementar, bom para filtros de spam e análise de sentimento.
- **K-Nearest Neighbor (K-NN)**: classifica uma nova observação com base na maioria dos seus K vizinhos mais próximos. Simples, eficaz e flexível, usado em recomendações e reconhecimento de padrões.
- **Regressão Linear**: encontra a melhor linha reta para modelar a relação entre variáveis. Simples e interpretável, usada para prever valores.
- **Árvore de Decisão**: modelo em forma de árvore que divide dados com base em critérios para classificação ou regressão. Vantagem principal é a interpretabilidade.
- **Modelagem por Agrupamento (Clustering)**: técnica não supervisionada para dividir dados em grupos (clusters) com base na similaridade. Útil para descobrir estrutura natural nos dados e obter insights, como segmentação de clientes.

Finalmente, a aula apresenta casos e tendências do mercado, destacando a empresa **Stitch Fix** como um exemplo notável do uso de IA e ciência de dados para personalizar a experiência de compras de moda.

A Aula 2 conclui que a IA é um ecossistema vasto que impulsiona inovação e eficiência, marcando uma era de colaboração entre máquina e mente humana.

**Notas Chave**

- IA aplica técnicas de análise avançada e lógica (incluindo ML) para interpretar eventos, dar suporte/automatizar decisões e tomar ações. É uma disciplina de engenharia computacional com foco em resolver problemas, não replicar a mente humana.
- O Machine Learning (ML) é um subconjunto da IA e, em si, possui subconjuntos como Predictive Analytics (Análise Preditiva) e Data Mining (Mineração de Dados). É importante notar que máquinas não "aprendem" no sentido humano, elas armazenam e computam, criando "modelos" a partir de dados.
- A eficácia de um algoritmo de ML depende muito da integridade da representação dos dados de entrada. DL se destaca por automatizar a extração de _features_ (características) relevantes.
- CRISP-DM é um modelo processual iterativo, não linear, com a possibilidade de pular fases ou retornar a fases anteriores conforme necessário no decorrer do projeto.
- A limpeza de dados é crucial antes da análise, pois dados imprecisos podem levar a conclusões errôneas.
- A analogia biológica do ML ajuda a entender a adaptação e melhoria dos algoritmos com base na exposição a mais dados e situações.
- A escolha do tipo de aprendizado (supervisionado, não supervisionado, etc.) e do algoritmo depende da natureza do problema, da disponibilidade de dados rotulados e do objetivo final (previsão, agrupamento, otimização, etc.).
- Algoritmos como K-NN são de "aprendizado preguiçoso" ("lazy learning"), onde a computação principal ocorre no momento da classificação, não em uma fase de treinamento explícita intensa.
- Regressão Linear funciona melhor com dados que exibem uma tendência linear e variáveis independentes.
- Árvores de Decisão podem sofrer de "overfitting" (sobreajuste) em dados com ruído, capturando padrões irrelevantes.
- Algoritmos de agrupamento (clustering) não supervisionados dependem da escolha de parâmetros (como o número de clusters K) e podem ser sensíveis a ruído/outliers.
- O caso da Stitch Fix ilustra como a combinação de IA com expertise humana pode criar experiências personalizadas e otimizar operações de negócio.
- A IA e o ML estão se tornando críticos para diferenciação e, por vezes, sobrevivência das organizações. Organizações com expertise em IA podem esperar retornos significativos ao capitalizar mudanças e disrupções sociais.
- Apesar do hype em torno da IA, muitas organizações enfrentam desafios na implementação, como integração, segurança e privacidade, que impedem a transição de protótipos para produção. É crucial focar em problemas de negócio reais e casos de uso alcançáveis para gerenciar expectativas e aumentar a taxa de sucesso dos projetos de IA.

**Glossário**

- **Algoritmo:** Um conjunto de regras ou procedimentos para resolver um problema ou realizar uma tarefa. No ML, algoritmos aprendem com dados.
- **Aprendizado Não Supervisionado:** Um tipo de ML onde o sistema identifica padrões e organiza dados sem rótulos ou orientação externa.
- **Aprendizado Semissupervisionado:** Um tipo de ML que utiliza um conjunto de dados grande, parte rotulada e parte não.
- **Aprendizado Supervisionado:** Um tipo de ML onde o sistema é treinado com dados rotulados (pares entrada-saída desejada) para fazer previsões.
- **Aprendizagem por Reforço:** Um tipo de ML onde o sistema aprende a tomar decisões por tentativa e erro, sendo recompensado por ações corretas.
- **Árvore de Decisão:** Um modelo de ML com estrutura em árvore usado para classificação e regressão, dividindo dados com base em critérios.
- **Big Data:** Refere-se ao imenso volume de dados - estruturados e não estruturados - que inundam os negócios e a tecnologia diariamente. É analisado para insights e decisões estratégicas. Caracterizado pelos 'V's: Volume, Velocidade, Variedade, Veracidade, Valor.
- **Classificador Naive Bayes:** Um modelo de ML baseado em probabilidade que assume independência entre atributos.
- **Clustering (Modelagem por Agrupamento):** Técnicas de aprendizado não supervisionado para dividir dados em grupos (clusters) com base em sua similaridade.
- **CNN (Convolutional Neural Network):** Um tipo popular de rede neural profunda (Deep Learning) especialmente eficaz para análise de dados visuais, que identifica automaticamente características relevantes.
- **Correlação:** Uma medida que descreve o grau de relação entre duas variáveis.
- **CRISP-DM (Cross-Industry Standard Process for Data Mining):** Um modelo de processo padrão para projetos de mineração de dados e análise preditiva, com seis fases.
- **Dados Estruturados:** Dados organizados de maneira clara e lógica, geralmente em tabelas com linhas e colunas, seguindo um modelo definido.
- **Dados Não Estruturados:** Informações que não seguem um modelo ou formato específico, como textos livres, imagens, vídeos e áudios.
- **Dados Semi Estruturados:** Dados que não se encaixam em tabelas rígidas, mas possuem algum nível de organização, como tags ou marcadores.
- **Dados Temporais (Séries de Dados Temporais):** Conjuntos de pontos de dados coletados em intervalos regulares ao longo do tempo.
- **Deep Learning (DL):** Um subconjunto do Machine Learning inspirado nos padrões de processamento de informação do cérebro humano. Utiliza numerosas camadas de algoritmos (redes neurais artificiais) para interpretar dados e automatizar a aprendizagem de características.
- **Desvio Padrão:** Uma medida de dispersão que indica o quanto os valores de um conjunto de dados variam em relação à média.
- **Distribuição Normal:** Uma distribuição de probabilidade que descreve como os valores de um conjunto de dados tendem a se agrupar em torno da média (também chamada Gaussiana).
- **Extração de Recursos:** O processo de identificar e selecionar um conjunto de características relevantes de um conjunto de dados para facilitar a análise. No DL, isso é frequentemente automatizado.
- **Feature Engineering:** Abordagem para construir características a partir de dados brutos, muitas vezes exigindo esforço humano e conhecimento específico do domínio.
- **Hadoop:** Um framework de software de código aberto que permite o processamento distribuído de grandes conjuntos de dados em clusters de computadores.
- **IA (Inteligência Artificial):** Aplica análise avançada e técnicas lógicas, incluindo machine learning, para interpretar eventos, dar suporte e automatizar decisões, e tomar ações.
- **K-Nearest Neighbor (K-NN):** Um algoritmo de ML usado para classificação e regressão com base na proximidade de pontos de dados ("semelhante atrai semelhante").
- **Linear Regression (Regressão Linear):** Um método estatístico para encontrar a melhor linha reta que modela a relação entre uma variável dependente e uma ou mais variáveis independentes.
- **Lucene:** Uma biblioteca de software de código aberto para busca e análise de texto.
- **Machine Learning (ML):** Uma área da inteligência artificial que se assemelha ao processo natural de aprendizagem, onde algoritmos aprimoram suas habilidades analisando e interpretando dados. É um subconjunto da IA.
- **Overfitting (Sobreajuste):** Um problema onde um modelo de ML tem um desempenho excelente nos dados de treinamento, mas não generaliza bem para dados não vistos (teste).
- **Teorema de Bayes:** Um método de cálculo de probabilidades condicionais.
- **Treinamento de Modelo:** O processo de usar dados para ensinar um algoritmo de ML a realizar uma tarefa específica, ajustando seus parâmetros internos.

Espero que este resumo detalhado, notas e glossário, baseados nas fontes fornecidas, sejam úteis para sua compreensão da Aula 2!
## Palavras Chaves:

1. Machine Learning 31
    
2. Dados 32
    
3. Ética 333333
    
4. Scikit-learn 34
    
5. Accuracy Score 35
    
6. Aprendizado Supervisionado 36
    
7. Aprendizado Não Supervisionado 37
    
8. Aprendizado por Reforço 38
    
9. Tipos de Dados 39
    
10. Alucinações 40
    

## Notas:

1. Machine Learning é uma área fundamental dentro da Inteligência Artificial, permitindo que computadores aprendam com dados e tomem decisões sem programação explícita41.
    
2. A análise ética e cuidadosa dos dados é crucial ao implementar soluções de Machine Learning, como ilustrado pelo caso da Target e a previsão de gravidez424242424242424242.
    
3. A preparação dos dados (limpeza, transformação e normalização) é uma etapa vital para garantir a precisão e a eficácia dos modelos de Machine Learning43.
    
4. A escolha do modelo de Machine Learning ideal depende dos dados disponíveis, do objetivo da análise e das limitações existentes44.
    
5. É fundamental testar a taxa de acerto de um modelo de Machine Learning para garantir que as previsões estejam corretas e ajustar o modelo, se necessário45.
    
6. "Alucinações" em Machine Learning são resultados incorretos ou irrelevantes, geralmente causados por dados mal treinados ou insuficientemente limpos46.
    
7. A demonstração prática em Python com Scikit-learn exemplificou como treinar um modelo para identificar padrões e fazer previsões a partir de um conjunto limitado de dados47474747.