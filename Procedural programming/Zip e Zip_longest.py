'''
Zip - Unindo iteráveis
Zip_longest = Itertools
'''
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
cidades_estados_completo = zip_longest(
    cidades, 
    estados, 
    fillvalue = 'MG',
)
cidades_estados_indice = zip(
    indice,
    cidades, 
    estados
)

print('\tZip:')
for valor in cidades_estados:
    print(valor)

print('\n\tZip_longest:')
for valor in cidades_estados_completo:
    print(valor)

print()

print('\n\tUsando o counter:')
# Desempacotando os valores
for indice, cidade, estado in cidades_estados_indice:
    print(indice, cidade, estado)