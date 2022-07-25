'''
Levantando exceções de funções
'''

# Passando o erro para a __main__
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise

try:
    n1, n2 = 1, 0
    print(divide(n1, n2))
except ZeroDivisionError as error:
    print(error)

print()

# Invocando o erro na própria função
def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('N2 não pode ser 0!')
    return n1 / n2

try:
    n1, n2 = 1, 0
    print(divide2(n1, n2))
except ValueError as error:
    print('Você está tentando dividir por zero!')
    print(error)