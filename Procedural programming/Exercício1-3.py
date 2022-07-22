'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
'''

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print('\tListas originais')
print('Lista A:', lista_a)
print('Lista B:', lista_b)

lista_soma = list(zip(lista_a, lista_b))
print('\n\tLista soma')
print('Tuplas com o zip:', lista_soma)

# Utilizando compreensão de lista para o cast e soma das listas de elementos
lista_soma = [sum(list(tupla)) for tupla in lista_soma]
print('Resultado 1:', lista_soma)

# Outra solução interessante seria apenas com:
lista_soma_ideal = [x + y for x, y in zip(lista_a, lista_b)]
print('Resultado 2:', lista_soma)