'''
Funções em Python - *args **kwargs
'''

def func(*args, **kwargs):
    args = list(args) # Cast de tupla para lista
    print('Nome contido na lista:', kwargs.get('nome'), kwargs.get('sobrenome'))
    for item in args:
        print(item, end = ' ')
    idade = kwargs.get('idade')
    if idade is not None:
        print('\nIdade contida na lista:', idade)
    else:
        print('\nIdade não existe!')

lista = [1, 2, 3, 4, 5]
func(*lista, nome = 'Gabriel', sobrenome = 'Costa', idade = 20) # Desempacotando a lista