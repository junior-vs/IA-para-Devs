
# Exemplos de Laços de Repetição em Python

# Laço for
print("Exemplo de laço for:")
for i in range(5):
    print(f"contador: {i}")

print("Exemplo de laço for:")
for i in range(1,5):
    print(f"contador: {i}")

print("Exemplo de laço for:")
for i in range(0, 10, 2):
    print(f"contador: {i}")


# Laço while
print("\nExemplo de laço while:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Uso do break
print("\nExemplo de uso do break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Uso do continue
print("\nExemplo de uso do continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Laços aninhados
print("\nExemplo de laços aninhados:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Laço for com lista
print("\nExemplo de laço for com lista:")
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Laço while com lista
print("\nExemplo de laço while com lista:")
frutas = ["maçã", "banana", "cereja"]
indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice += 1
