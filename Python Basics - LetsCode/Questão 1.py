'''
QUESTÃO 1

Faça um programa que peça ao usuário um número
e imprima todos os números de um até o número que 
o usuário informar.
'''

n = input('Informe um número natural: ')
if not n.isdigit():
    print('O valor digitado precisa ser um inteiro!...')
else:
    n = int(n)
    for number in range(1, n + 1):
        print(number, end=' ')