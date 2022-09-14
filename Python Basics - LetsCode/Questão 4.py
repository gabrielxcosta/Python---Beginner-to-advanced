'''
QUESTÃO 4

Faça um programa que peça 2 números inteiros e um número real, 
calcule e mostre:

a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.
'''
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

n1 = input('Informe um número inteiro: ')
if not n1.isdigit():
    raise TypeError('O valor necessita ser um inteiro!...')

n2 = input('Informe um número real: ')
if not isfloat(n2):
    raise TypeError('O valor necessita ser um real!...')

n1 = int(n1)
n2 = float(n2)

# a)
a = (2 * n1) * (n2 / 2)

# b)
b = (3 * n1) + a

# c)
c = a ** 3

print(f'a) {a}')
print(f'b) {b}')
print(f'c) {c}')