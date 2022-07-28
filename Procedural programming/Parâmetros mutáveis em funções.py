'''
Mutável: listas, dicionários
Imutável: tuplas, strings, números, True, False, None
'''
def lista_de_clientes(lista_clientes, lista = None):
    if lista is None:
        lista = []
    lista.extend(lista_clientes)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)