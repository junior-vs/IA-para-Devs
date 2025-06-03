# Exemplos de coleções em Python

# Listas
# Uma lista é uma coleção ordenada e mutável de elementos.
lista = [1, 2, 3, 4, 5]
print("Lista:", lista)

# Tuplas
# Uma tupla é uma coleção ordenada e imutável de elementos.
tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)

# Conjuntos
# Um conjunto é uma coleção não ordenada e não permite elementos duplicados.
conjunto = {1, 2, 3, 4, 5}
print("Conjunto:", conjunto)

# Dicionários
# Um dicionário é uma coleção não ordenada de pares chave-valor.
dicionario = {'a': 1, 'b': 2, 'c': 3}
print("Dicionário:", dicionario)

# Módulo collections
# O módulo collections oferece tipos de dados especializados como namedtuple, deque, Counter, OrderedDict e defaultdict.

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

# namedtuple
# Cria uma tupla com nomes para os campos.
Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
pessoa = Pessoa(nome='João', idade=30)
print("namedtuple:", pessoa)

# deque
# Cria uma lista com desempenho otimizado para inserções e remoções nas extremidades.
fila = deque(['a', 'b', 'c'])
fila.append('d')
fila.appendleft('z')
print("deque:", fila)

# Counter
# Cria um dicionário para contar elementos.
contador = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print("Counter:", contador)

# OrderedDict
# Cria um dicionário que mantém a ordem de inserção dos elementos.
ord_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("OrderedDict:", ord_dict)

# defaultdict
# Cria um dicionário que fornece um valor padrão para chaves inexistentes.
def_dict = defaultdict(int)
def_dict['a'] += 1
print("defaultdict:", def_dict)
