'''
QUESTÃO 2

Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. 
'''

import os

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

n = input('Entrada: ')
if not isfloat(n):
    print('O valor digitado precisa ser um número!...')
else:
    os.system('cls')
    n = float(n)
    if n >= 0 and n <= 25:
        print(f'Entrada: {n} | Saída: [0, 25]')
    elif n > 25 and n <= 50:
        print(f'Entrada: {n} | Saída: (25, 50]')
    elif n > 50 and n <= 75:
        print(f'Entrada: {n} | Saída: (50, 75]')
    elif n > 75 and n <= 100:
        print(f'Entrada: {n} | Saída: (75, 100]')
    else:
        print(f'Entrada: {n} | Saída: Fora de intervalo')