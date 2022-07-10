'''
Desempacotamento de listas 
'''

lista = ['Gabriel', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1, n2 , n3, *outra_lista, ultimo = lista
print(n1, n2, n3, outra_lista, ultimo)