
print(" Exemplos de processos mais utilizados com listas em Python")

print(" 1. Criação de listas")
lista = [1, 2, 3, 4, 5]

print(" 2. Acesso a elementos")
print(lista[0])      # Primeiro elemento
print(lista[-1])     # Último elemento

print(" 3. Fatiamento (slicing)")
print(lista[1:4])    # Elementos do índice 1 ao 3
print(lista[:3])     # Três primeiros
print(lista[::2])    # De dois em dois

print(" 4. Adição de elementos")
print(lista)
lista.append(6)         # Adiciona ao final
print(lista)
lista.insert(2, 99)     # Insere no índice 2
print(lista)
lista.extend([7, 8])    # Adiciona múltiplos elementos

print(" 5. Remoção de elementos")
print(lista)
lista.remove(3)     # Remove o valor 3
print(lista)
lista.pop()         # Remove o último
print(lista)
lista.pop(1)        # Remove o índice 1
print(lista)
del lista[0]        # Remove o índice 0
print(lista)

print("6. Busca e verificação")
print(4 in lista)       # Verifica se 4 está na lista
print(lista.index(4))   # Retorna o índice do valor 4
print(lista.count(4))   # Conta quantas vezes 4 aparece

print("7. Ordenação e reversão")
print(lista)
lista.sort()            # Ordena em ordem crescente
print(lista)
lista.sort(reverse=True)  # Ordem decrescente
print(lista)
lista.reverse()         # Inverte a ordem atual
print(lista)

print("8. Cópia de listas")
nova_lista = lista.copy()

print("9. Iteração")
for item in lista:
    print(item)

print("10. List Comprehension (compreensão de listas)")
quadrados = [x**2 for x in lista]
print(quadrados)