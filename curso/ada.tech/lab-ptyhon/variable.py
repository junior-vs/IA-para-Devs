# Isso é um comentário de uma linha
""" exemplo de comentário
de várias linhas

Nesse codigo aprensetamos variáveis, operadores e tipos de dados

var1 = 12

var2 = 30

var3 = var1 + var2

print(var3)

var3 = var3 / 2

print(var3)

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)
x = 4.2

y = 10

z = "42"

expected = not (((x * y == z) and not (x < y)) or y % 2 == 0)
result = not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z))))

print(expected)
print(result)
"""

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print(resposta)