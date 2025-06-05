# Exemplos de List Comprehension em Python

# 🧠 O que é List Comprehension?
# List Comprehension é uma forma concisa de criar listas a partir de iteráveis, usando uma sintaxe compacta e legível.

# 📌 Sintaxe básica
quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]

# ✅ Com condição (if)
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# ✅ Com if-else na expressão
rotulos = ["par" if x % 2 == 0 else "ímpar" for x in range(5)]
print(rotulos)  # ['par', 'ímpar', 'par', 'ímpar', 'par']

# ✅ Com múltiplos for
combinacoes = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(combinacoes)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 🆚 Vantagens sobre for tradicional
# List Comprehension é mais conciso e performático, enquanto o for tradicional é mais flexível para lógica complexa.

# Exemplo com for tradicional
quadrados_tradicional = []
for x in range(5):
    quadrados_tradicional.append(x**2)
print(quadrados_tradicional)  # [0, 1, 4, 9, 16]
