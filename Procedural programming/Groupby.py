'''
Agrupando elementos
'''
from itertools import groupby, tee

alunos = [
    {'nome' : 'Luiz', 'nota' : 'A'},
    {'nome' : 'Letícia', 'nota' : 'B'},
    {'nome' : 'Fabrício', 'nota' : 'A'},
    {'nome' : 'Rosemary', 'nota' : 'C'},
    {'nome' : 'Joana', 'nota' : 'D'},
    {'nome' : 'João', 'nota' : 'A'},
    {'nome' : 'Eduardo', 'nota' : 'B'},
    {'nome' : 'André', 'nota' : 'A'},
    {'nome' : 'Anderson', 'nota' : 'C'},
    {'nome' : 'José', 'nota' : 'B'}
]

# Ordenando o dicionário pela nota do aluno
ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    v_a1, v_a2 = tee(valores_agrupados) # Fazendo duas cópias do iterador
    print(f'Agrupamento: {agrupamento}')
    for aluno in v_a1:
        print(aluno)
    quantidade = len(list(v_a2))
    if quantidade > 1:
        print(f'{quantidade} alunos tiraram a nota {agrupamento}')
        print()
    else:
        print(f'{quantidade} aluno tirou a nota {agrupamento}')
        print()