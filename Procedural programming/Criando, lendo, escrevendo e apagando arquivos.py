'''
Criando, lendo, escrevendo e apagando arquivos em Python
'''
import os

file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# Voltando o cursor ao começo do arquivo e lendo as linhas
file.seek(0, 0)
print('Lendo linhas:')
print(file.read())

print('#########\n')

# Voltando o cursor ao começo do arquivo e lendo as linhas uma por uma
file.seek(0, 0)
print('Lendo linhas:')
print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')

print('\n#########\n')

# Inserindo as linhas do arquivo em uma lista com o readlines()
file.seek(0, 0)
print(file.readlines())
file.close()

# Deletando um arquivo com o módulo OS e a função remove()
os.remove('abc.txt')