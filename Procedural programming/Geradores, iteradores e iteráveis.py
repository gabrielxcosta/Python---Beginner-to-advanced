'''
Geradores, iteradores e iteráveis em Python
'''
from sys import getsizeof

nome = 'Gabriel Costa'
l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
print('Tamanho da memória alocada para a lista:', getsizeof(l1), 'bites')
print('Tamanho da memória alocada para a gerador:', getsizeof(l2), 'bites')
iterador = iter(nome)
gerador = (letra for letra in nome)

# lists, tuples, str -> Sequências -> Iteráveis