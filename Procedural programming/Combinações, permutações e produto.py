'''
Combinations, permutations e product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rosa']
print('Lista original:', pessoas)

print('\n\tCombinações:')
for grupo in combinations(pessoas, 2):
    print(grupo)

print('\n\tPermutações:')
for grupo in permutations(pessoas, 2):
    print(grupo)

print('\n\tProduto:')
for grupo in product(pessoas, repeat = 2):
    print(grupo)