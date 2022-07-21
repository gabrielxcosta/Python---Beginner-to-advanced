'''
Compreensão de dicionários em Python
'''
from numpy import conjugate


lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
]

d1 = {x : y for x, y in lista}
print('Dicionário:', d1)
conjunto = {x for x in range(11)}
print('Conjunto:', conjunto)