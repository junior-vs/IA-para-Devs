
# Exemplos criativos de uso de dicionários em Python

# 1. Dicionário simples
alunos = {
    'João': 8.5,
    'Maria': 9.0,
    'Pedro': 7.5
}
print(alunos)

# 2. Dicionário aninhado
turma = {
    'Turma A': {'João': 8.5, 'Maria': 9.0},
    'Turma B': {'Pedro': 7.5, 'Ana': 8.0}
}
print(turma)

# 3. Contador com dicionário
from collections import Counter
frutas = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
contador_frutas = Counter(frutas)
print(contador_frutas)

# 4. Mapeamento dinâmico
quadrados = {x: x**2 for x in range(10)}
print(quadrados)

# 5. Uso com funções
def criar_dicionario(*args):
    return {arg: len(arg) for arg in args}

palavras = criar_dicionario('python', 'dicionário', 'criativo')
print(palavras)

# 6. Simulação de switch-case
def switch_case(opcao):
    casos = {
        'a': 'Opção A selecionada',
        'b': 'Opção B selecionada',
        'c': 'Opção C selecionada'
    }
    return casos.get(opcao, 'Opção inválida')

print(switch_case('a'))
print(switch_case('d'))

# 7. Dicionário com valores padrão
from collections import defaultdict
notas = defaultdict(lambda: 'Nota não disponível')
notas['João'] = 8.5
print(notas['João'])
print(notas['Maria'])

# 8. Dicionário de dicionários
empresa = {
    'Departamento de TI': {'João': 'Desenvolvedor', 'Maria': 'Analista'},
    'Departamento de RH': {'Pedro': 'Recrutador', 'Ana': 'Assistente'}
}
print(empresa)

# 9. Iteração sobre dicionários
for aluno, nota in alunos.items():
    print(f'Aluno: {aluno}, Nota: {nota}')

# 10. Atualização de dicionários
alunos.update({'Carlos': 8.0})
print(alunos)
