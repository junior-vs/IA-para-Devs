
# Exemplos de Estruturas Condicionais em Python

# 1. Estrutura if
numero = 10
if numero > 5:
    print("O número é maior que 5")

# 2. Estrutura if-else
numero = 3
if numero > 5:
    print("O número é maior que 5")
else:
    print("O número é menor ou igual a 5")

# 3. Estrutura if-elif-else
numero = 7
if numero > 10:
    print("O número é maior que 10")
elif numero > 5:
    print("O número está entre 6 e 10")
else:
    print("O número é 5 ou menor")

# 4. Estruturas condicionais aninhadas
numero = 8
if numero > 5:
    if numero % 2 == 0:
        print("O número é maior que 5 e é par")
    else:
        print("O número é maior que 5 e é ímpar")
else:
    print("O número é 5 ou menor")

# 5. Estrutura if com múltiplas condições
idade = 20
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# 6. Estrutura if com operador ternário
idade = 17
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Você é {status}")

# 7. Estrutura if com valores booleanos
ativo = True
if ativo:
    print("A conta está ativa")
else:
    print("A conta está inativa")
