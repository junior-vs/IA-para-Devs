## 1. DEFINIÇÃO E FUNDAMENTOS

**Definição clara e concisa**

A **regressão linear** é uma técnica estatística fundamental usada para modelar e quantificar a relação entre uma variável dependente (o que queremos prever) e uma ou mais variáveis independentes (os fatores que usamos para prever)[1](https://www.ibm.com/br-pt/think/topics/linear-regression)[2](https://hub.asimov.academy/blog/regressao-linear/)[3](https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear)[4](https://aws.amazon.com/pt/what-is/linear-regression/). Quando há apenas uma variável independente, chamamos de _regressão linear simples_; com duas ou mais, de _regressão linear múltipla_.

**Intenção e motivação**

O objetivo central da regressão linear é prever valores futuros da variável dependente com base em valores conhecidos das variáveis independentes, além de entender a força e a direção dessa relação. Por exemplo, podemos prever o preço de uma casa (variável dependente) a partir de seu tamanho, localização e número de quartos (variáveis independentes).

**Importância e aplicações**

A regressão linear é amplamente utilizada porque oferece uma maneira intuitiva e eficiente de transformar dados em previsões e insights práticos. Empresas usam para estimar vendas a partir de gastos em publicidade, cientistas para prever crescimento de plantas com base em nutrientes, e analistas de dados para identificar tendências em datasets clássicos como o _Boston Housing_ ou o _Iris_[1](https://www.ibm.com/br-pt/think/topics/linear-regression)[2](https://hub.asimov.academy/blog/regressao-linear/)[4](https://aws.amazon.com/pt/what-is/linear-regression/). Sua simplicidade facilita a interpretação dos resultados e a comunicação com públicos não técnicos.

**Analogia do mundo real**

Imagine que você quer saber como a quantidade de horas estudadas afeta a nota de um exame. Se você plotar em um gráfico as horas estudadas (eixo X) e as notas (eixo Y), a regressão linear encontra a linha que melhor resume essa relação: quanto mais você estuda, maior tende a ser sua nota – essa tendência é capturada pela inclinação da linha.

**Conceitos base necessários**

Para compreender a regressão linear, é importante ter familiaridade com:

- **Variáveis dependentes e independentes**
	- **Variável dependente** é o resultado ou resposta que queremos prever ou explicar em um experimento ou análise (por exemplo, a nota de um aluno).  
	- **Variável independente** é o fator ou característica que usamos para tentar explicar ou prever a variável dependente (por exemplo, horas de estudo).  
	- Em resumo: a variável dependente depende da independente.

- **Função linear (reta)**  
    - É uma função matemática da forma $f(x)=a⋅x$ ou $f(x) = a \cdot x$ ou $f(x)=a⋅x$ , onde $a$ é um número real diferente de zero. Seu gráfico é uma reta que passa pela origem $(0,0)$, indicando uma relação de proporcionalidade direta entre $x$ e $f(x)$. [2](https://brasilescola.uol.com.br/matematica/funcao-linear.htm)[3](https://www.todamateria.com.br/funcao-linear/)[4](https://mundoeducacao.uol.com.br/matematica/funcao-linear.htm).
    
- **Noção de erro e resíduos**  
    - Erro ou resíduo é a diferença entre o valor observado (real) e o valor previsto pelo modelo. 
    
- **Distribuição normal**  
    - É uma distribuição de probabilidade contínua, simétrica em torno da média, com formato de "sino". Muitos fenômenos naturais seguem essa distribuição, e ela é fundamental para inferência estatística
    
- **Conceitos de correlação e causalidade**  
    - Correlação mede a associação ou relação entre duas variáveis, indicando se elas variam juntas. Causalidade implica que uma variável causa diretamente a outra. Correlação não implica causalidade, ou seja, duas variáveis podem estar relacionadas sem que uma cause a outra.
    
- **Método dos mínimos quadrados**  
    - É uma técnica para ajustar uma linha de regressão que minimiza a soma dos quadrados dos resíduos, ou seja, minimiza a soma de $(yi−y^i)2$ . É o método padrão para encontrar os coeficientes da regressão linear.

   

---

## 2. ASPECTOS TÉCNICOS

**Formulação matemática**

A equação da regressão linear simples é:

$$

Y = \beta_0 + \beta_1 X + \epsilon
$$

Onde:

- y: variável dependente (resposta)
    
- x: variável independente (explicativa)
    
- $\beta_0$ : intercepto (valor de y quando X=0)
    
- $\beta_1$: coeficiente angular (quanto Y varia a cada unidade de X)
    
- $\epsilon$ : termo de erro (diferença entre o valor observado e o previsto)[2](https://hub.asimov.academy/blog/regressao-linear/)[5](https://blog.betrybe.com/regressao-linear-simples/)[3](https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear)
    

O método mais comum para estimar β0\beta_0β0 e β1\beta_1β1 é o **método dos mínimos quadrados**, que minimiza a soma dos quadrados dos resíduos (ei=yi−y^ie_i = y_i - \hat{y}_iei=yi−y^i).

**Pressupostos e limitações**

Para que a regressão linear produza resultados confiáveis, alguns pressupostos precisam ser atendidos[6](https://sweet.ua.pt/pedrocruz/bioestatistica/rl-pressupostos.html)[7](https://analisemacro.com.br/data-science/por-que-nao-usar-uma-regressao-linear/)[3](https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear):

- **Linearidade**: a relação entre XXX e YYY é linear.
    
- **Independência dos erros**: os resíduos (ϵ\epsilonϵ) são independentes entre si.
    
- **Normalidade dos erros**: os resíduos seguem uma distribuição normal com média zero.
    
- **Homoscedasticidade**: a variância dos resíduos é constante para todos os valores de XXX.
    
- **Ausência de multicolinearidade** (na regressão múltipla): as variáveis independentes não são altamente correlacionadas entre si.
    

**Considerações importantes**

- **Sensibilidade a outliers**: valores extremos podem distorcer a linha de regressão, tornando o modelo menos confiável[7](https://analisemacro.com.br/data-science/por-que-nao-usar-uma-regressao-linear/).
    
- **Correlação não implica causalidade**: uma relação linear não garante que uma variável cause a outra.
    
- **Limitações para relações não-lineares**: se a relação entre as variáveis não for linear, outros modelos podem ser mais adequados.
    

**Dicas práticas**

- Sempre visualize os dados antes de ajustar o modelo.
    
- Verifique os resíduos para garantir que os pressupostos estão sendo atendidos (ex: gráfico de resíduos vs. valores ajustados, QQ plot para normalidade dos resíduos)[6](https://sweet.ua.pt/pedrocruz/bioestatistica/rl-pressupostos.html).
    
- Use datasets conhecidos, como o _Boston Housing_, para praticar e validar o entendimento do processo.
    

**Motivação final**

A regressão linear é uma das ferramentas mais poderosas e acessíveis para quem está começando em análise de dados e estatística. Dominar seus fundamentos abre portas para técnicas mais avançadas e aplicações em quase todas as áreas do conhecimento. Continue praticando, questione os resultados e explore suas aplicações em diferentes contextos!

---

**Warning comum:**  
Muitos estudantes confundem correlação com causalidade e negligenciam a análise dos resíduos. Sempre questione se os pressupostos do modelo estão sendo respeitados antes de confiar nas previsões!

1. [https://www.ibm.com/br-pt/think/topics/linear-regression](https://www.ibm.com/br-pt/think/topics/linear-regression)
2. [https://hub.asimov.academy/blog/regressao-linear/](https://hub.asimov.academy/blog/regressao-linear/)
3. [https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear](https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear)
4. [https://aws.amazon.com/pt/what-is/linear-regression/](https://aws.amazon.com/pt/what-is/linear-regression/)
5. [https://blog.betrybe.com/regressao-linear-simples/](https://blog.betrybe.com/regressao-linear-simples/)
6. [https://sweet.ua.pt/pedrocruz/bioestatistica/rl-pressupostos.html](https://sweet.ua.pt/pedrocruz/bioestatistica/rl-pressupostos.html)
7. [https://analisemacro.com.br/data-science/por-que-nao-usar-uma-regressao-linear/](https://analisemacro.com.br/data-science/por-que-nao-usar-uma-regressao-linear/)
8. [https://ebaconline.com.br/blog/regressao-linear-seo](https://ebaconline.com.br/blog/regressao-linear-seo)
9. [https://www.totvs.com/blog/inteligencia-dados/regressao-linear/](https://www.totvs.com/blog/inteligencia-dados/regressao-linear/)
10. [https://repositorio.enap.gov.br/bitstream/1/4788/1/Livro_Regress%C3%A3o%20Linear.pdf](https://repositorio.enap.gov.br/bitstream/1/4788/1/Livro_Regress%C3%A3o%20Linear.pdf)
11. [https://www.educamaisbrasil.com.br/enem/matematica/funcao-linear](https://www.educamaisbrasil.com.br/enem/matematica/funcao-linear)
12. [https://brasilescola.uol.com.br/matematica/funcao-linear.htm](https://brasilescola.uol.com.br/matematica/funcao-linear.htm)
13. [https://www.todamateria.com.br/funcao-linear/](https://www.todamateria.com.br/funcao-linear/)
14. [https://mundoeducacao.uol.com.br/matematica/funcao-linear.htm](https://mundoeducacao.uol.com.br/matematica/funcao-linear.htm)
15. [https://www.teachy.com.br/resumos/ensino-fundamental/9ano/matematica/resumo-de-conteudo-funcoes-lineares-Expositiva](https://www.teachy.com.br/resumos/ensino-fundamental/9ano/matematica/resumo-de-conteudo-funcoes-lineares-Expositiva)
16. [https://www.youtube.com/watch?v=ZR1Z6WBE_GU](https://www.youtube.com/watch?v=ZR1Z6WBE_GU)
17. [https://www.youtube.com/watch?v=72ddxNh47J8](https://www.youtube.com/watch?v=72ddxNh47J8)
18. [https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_linear](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_linear)
