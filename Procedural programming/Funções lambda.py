'''
Funções lambda ou funções anônimas
'''
catalogo = [ # Produto e preço
    ['Produto 1', 13.85],
    ['Produto 2', 15.60],
    ['Produto 3', 19.84],
    ['Produto 4', 11.47],
    ['Produto 5', 12.61]
]

catalogo.sort(key = lambda item: item[1]) # Ordenando do menor valor ao maior
print(catalogo)