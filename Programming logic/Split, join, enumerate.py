'''
Split, join e enumerate
* split() - Dividir uma string #str
* join() - Juntar uma lista #str
* enumerate() - Enumerar elementos da lista #Iteráveis
'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print("Separando a lista com o delimitador ' ' ->", lista_1)
print("Separando a lista com o delimitador ',' ->", lista_2)

print()

# Contando qts vezes cada palavra apareceu na frase:
for palavra in lista_1:
    print(f'A palavra {palavra} apareceu {lista_1.count(palavra)}x na frase')

print()

# Utilizando join para juntar uma lista em uma string com um separador 
string_2 = ','.join(lista_2)
print("Juntando uma lista em uma string com o separador ',' ->", string_2)

print()

# Enumerando listas com enumerate
frase = 'O Brasil é penta.'
lista = frase.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor)
