'''
Filter em Python
'''
from Dados import produtos, pessoas, lista

print('Trabalhando com a função filter()')
print('\nLista original:', lista)

nova_lista = list(filter(lambda x: x > 5, lista))
print('Valores > que 5:', nova_lista)

print('\n\tProdutos com valor > R$50\n')
nova_lista2 = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista2:
    print(produto)