'''
Utilizando o map() em Python
'''
from Dados import produtos, pessoas, lista

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

print('Trabalhando com a função map()')
print('\nLista original:', lista)

nova_lista = map(lambda x: x * 2, lista)
print('Novo objeto gerado do mapeamento:', nova_lista)
nova_lista = list(nova_lista)
print('Cast para lista do mapeamento feito:', nova_lista)

print()

# Printando cada preço de 'produtos' usando map()
precos = map(lambda p: p['preco'], produtos)
print('\tProdutos e preços:')
for indice, preco in enumerate(precos):
    print(f'Produto {indice + 1} = R${preco}')

print()

# Aumentando o preço de cada produto em 5%
novos_produtos = map(aumenta_preco, produtos)
novos_produtos = [p['preco'] for p in novos_produtos]
print('\tAumentando o preço dos produtos em 5%:')
for indice, preco in enumerate(novos_produtos):
    print(f'Produto {indice + 1} = R${preco}')

print()

# Printando os nome contidos em 'pessoas' usando map()
print('\tNomes das pessoas:')
nomes = map(lambda n: n['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)