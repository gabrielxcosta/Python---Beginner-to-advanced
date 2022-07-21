'''
Compreensão de lista em Python
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [2 * valor for valor in lista]

print('Lista original:', lista)
print('Lista duplicada:', lista2)

# Usando tuplas para criar coordenadas com a lista original
lista3 = [(x, y) for x in lista for y in range(10)]
print('Lista coordenadas:', lista3)

print()

# Lista de strings
lista_strings = ['Marrocos', 'Angola', 'Nigéria', 'Egito']
print('Lista de strings:', lista_strings)

# Trocando a letra 'a' nas palavras por '@' usando list comprehension
lista_strings_replace = [v.replace('a', '@') for v in lista_strings]
print('Lista de strings alterada:', lista_strings_replace)

print()

# Trabalhando tuplas usando list comprehension
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
)

print('Tupla original:', tupla)
chave_valor = [(x, y) for x, y in tupla]
print('Lista de chaves-valores da tupla:', chave_valor)
chave_valor = dict(chave_valor)
print('Dicionário com a lista da tupla:', chave_valor)