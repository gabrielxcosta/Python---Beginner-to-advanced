'''
Listas em Python:
1. Fatiamento
2. append, insert, pop, del, clear, extend, +
3. min, max
4. range
'''
#         0    1    2    3    4 
lista = ['A', 'B', 'C', 'D', 'E']
#   -     5    4    3    2    1

# 1.
print('Lista antes do fatiamento ->', lista)
print('Lista depois do fatiamento ->', lista[: 3 :])

print()

# 2.
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2 # Concatenando listas
print('Lista 1 ->', lista_1)
print('Lista 2 ->', lista_2)
print('Concatenando listas (operador +) ->', lista_3)

print()

# Podemos fazer isso com o método .extend(elemento/lista) -> Extende a lista com outra lista ou elemento
print('Lista 1 ->', lista_1)
lista_1.extend('a')
print('Extendendo a lista 1 (.extend) ->', lista_1)

print()

# Podemos incluir um elemento ou valores ao final de uma lista com o método .append(elemento)
print('Lista 2 ->', lista_2)
lista_2.append('b')
print('Incluindo valores ao final da lista 2 (.append) ->', lista_2)

print()

# Podemos incluir um elemento em qualquer posição da lista com o método .insert(índice da posição, valor)
print('Lista 2 ->', lista_2)
lista_2.insert(0, 'banana')
print('Inserindo elementos em qlqr posição da lista 2 (.insert) ->', lista_2)

print()

# Removendo um elemento de alguma posição da lista com o método .pop(índice da posição)
print('Lista 1 ->', lista_1)
lista_1.pop()
print('Removendo um elemento do final da lista 1 (.pop) ->', lista_1)

print()

# Deletando elementos da lista com o método .del(fatias da lista/elementos)
print('Lista 3 ->', lista_3)
del(lista_3[ : 2])
print('Deletando elementos da lista 3 ->', lista_3)

print()

# 4.
# Criando listas usando a função built-in list() -> Torna um iterável ou um conjunto deles em uma lista
lista_4 = list(range(0, 11))
print('Criando a lista 4 com range() e list() ->', lista_4)