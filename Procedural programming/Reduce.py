'''
Utilizando o reduce() em Python
'''
from Dados import produtos, pessoas, lista
from functools import reduce

print(f'Lista original: {lista}')

# Acumulando sobre uma lista
soma_lista = 0
for valor in lista:
    soma_lista += valor
print(f'Acumulando sobre uma lista: {soma_lista}')

# Acumulando sobre uma lista com reduce
soma_lista_reduce = reduce(lambda ac, i: i + ac, lista, 0)
print(f'Acumulando sobre uma lista com o reduce: {soma_lista_reduce}')

print()

# Acumulando os preços dos produtos
soma_precos = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
precos = map(lambda p: p['preco'], produtos)
for indice, preco in enumerate(precos):
    print(f'Produto {indice + 1}: {preco}')
print('\nSoma dos preços com reduce:', round(soma_precos, 2))

print()

# Fazendo a média de idades das pessoas
soma_idade = reduce(lambda ac, i: ac + i['idade'], pessoas, 0)
media_idade = soma_idade / len(pessoas)
print(f'Média das idades das pessoas: {media_idade}')
