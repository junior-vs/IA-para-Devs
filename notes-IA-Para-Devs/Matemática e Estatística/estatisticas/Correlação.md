### 🔍 **O que é Correlação?**

Correlação é uma **medida estatística** que indica **como duas variáveis estão relacionadas**. Ou seja, mostra **se e como uma variável muda quando a outra muda**.

---

### 📌 **Por que é importante no Machine Learning?**

- Ajuda a **entender relacionamentos entre variáveis** antes de treinar modelos.
    
- Permite **remover variáveis redundantes** (altamente correlacionadas entre si), o que pode melhorar o desempenho do modelo.
    
- Pode **sugerir relações causais** (mas não confirma causalidade!).
    
- É útil na **seleção de features (variáveis)** relevantes para o modelo.
    

---

### 📈 **Como funciona?**

A correlação mais comum é o **coeficiente de correlação de Pearson**, que mede a **relação linear** entre duas variáveis numéricas.  
Seu valor varia entre:

- **+1** → correlação **positiva perfeita** (quando uma aumenta, a outra também aumenta proporcionalmente).
    
- **0** → **nenhuma correlação linear**.
    
- **-1** → correlação **negativa perfeita** (quando uma aumenta, a outra diminui proporcionalmente).
    

#### ✅ Fórmula do Coeficiente de Correlação de Pearson (r):

$$r=∑(xi−xˉ)(yi−yˉ)∑(xi−xˉ)2⋅∑(yi−yˉ)2r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \cdot \sqrt{\sum (y_i - \bar{y})^2}}$$

$$xi,yix_i, y_i$$: valores individuais das variáveis
    
$$xˉ,yˉ\bar{x}, \bar{y}$$: médias das variáveis
    

---

### 📚 **Exemplo Prático:**

Imagine que você quer saber se **mais horas de estudo** levam a **notas mais altas** em uma prova.

- Se os dados mostrarem que, conforme as horas de estudo aumentam, as notas também aumentam, então a correlação é **positiva**.
    
- Se mais estudo levar a notas mais baixas (hipoteticamente), a correlação é **negativa**.
    
- Se não houver padrão claro, a correlação será **próxima de zero**.
    

---

### ⚠️ **Importante:**

> **Correlação ≠ Causalidade!**  
> Só porque duas variáveis estão correlacionadas, **não significa que uma causa a outra**.

---

## ✅ Exemplo 1: Correlação Positiva

### 🔢 Dados:

|Estudo (X - horas)|Nota (Y - pontos)|
|---|---|
|1|2|
|2|4|
|3|6|
|4|8|
|5|10|

Aqui parece haver uma **relação direta**: quanto mais estuda, maior a nota.

### 🧮 Passos:

1. **Calcular a média de X e Y**:
    
    $$xˉ=1+2+3+4+55=3\bar{x} = \frac{1+2+3+4+5}{5} = 3$$
        
    $$yˉ=2+4+6+8+105=6\bar{y} = \frac{2+4+6+8+10}{5} = 6$$
        
2. **Montar a tabela com os componentes da fórmula**:
    

| X   | Y   | X - 𝑥̄ | Y - 𝑦̄ | (X-𝑥̄)(Y-𝑦̄) | (X-𝑥̄)² | (Y-𝑦̄)² |
| --- | --- | ------- | ------- | -------------- | -------- | -------- |
| 1   | 2   | -2      | -4      | 8              | 4        | 16       |
| 2   | 4   | -1      | -2      | 2              | 1        | 4        |
| 3   | 6   | 0       | 0       | 0              | 0        | 0        |
| 4   | 8   | 1       | 2       | 2              | 1        | 4        |
| 5   | 10  | 2       | 4       | 8              | 4        | 16       |
|     |     |         |         | **∑=20**       | **∑=10** | **∑=40** |

3. **Aplicar a fórmula**:
    

$$
r=∑(xi−xˉ)(yi−yˉ)∑(xi−xˉ)2⋅∑(yi−yˉ)2=2010⋅40=20400=2020=1r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \cdot \sqrt{\sum (y_i - \bar{y})^2}} = \frac{20}{\sqrt{10} \cdot \sqrt{40}} = \frac{20}{\sqrt{400}} = \frac{20}{20} = 1
$$
📌 **Resultado: r = 1 (Correlação positiva perfeita)**

---

## ❌ Exemplo 2: Correlação Negativa

### 🔢 Dados:

|Estudo (X)|Erros na prova (Y)|
|---|---|
|1|10|
|2|8|
|3|6|
|4|4|
|5|2|

Quanto mais estuda, **menos erra**.

### Passos:

$$
xˉ=3\bar{x} = 3, yˉ=6\bar{y} = 6
$$
    
- Mesma estrutura da tabela de antes
    

|X|Y|X - 𝑥̄|Y - 𝑦̄|(X-𝑥̄)(Y-𝑦̄)|(X-𝑥̄)²|(Y-𝑦̄)²|
|---|---|---|---|---|---|---|
|1|10|-2|4|-8|4|16|
|2|8|-1|2|-2|1|4|
|3|6|0|0|0|0|0|
|4|4|1|-2|-2|1|4|
|5|2|2|-4|-8|4|16|
|||||**∑=-20**|**∑=10**|**∑=40**|

$$
r=−2010⋅40=−2020=−1r = \frac{-20}{\sqrt{10 \cdot 40}} = \frac{-20}{20} = -1
$$

📌 **Resultado: r = -1 (Correlação negativa perfeita)**
 