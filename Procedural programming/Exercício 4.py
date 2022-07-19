'''
Exercício 4 - Fizz Buzz
'''
from random import randint

def FizzBuzz(valor):
    if type(valor) != int:
        return valor
    if valor % 3 == 0 and valor % 5 == 0:
        return 'FizzBuzz'
    if valor % 5 == 0:
        return 'Buzz'
    if valor % 3 == 0:
        return 'Fizz'
    return valor

imprime = lambda x: print('Resultado:', x)
for i in range(101):
    aleatorio = randint(0, 101)
    imprime(FizzBuzz(aleatorio))
