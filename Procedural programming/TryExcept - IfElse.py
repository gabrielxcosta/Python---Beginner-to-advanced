'''
Fazendo a multiplicação de dois números pegando o input do usuário
'''

def converte_numero(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            pass    


while True:
    numero = converte_numero(input('Informe o número: '))
    if numero is not None:
        print(numero * 5)
    else:
        print('O valor informado não é um número!')
    print()