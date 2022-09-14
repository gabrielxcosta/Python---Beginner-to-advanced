'''
QUESTÃO 3

Crie uma função que recebe o valor do raio de um círculo como parâmetro 
e retorna o valor da área desse círculo. Lembrando que a área de círculo 
é dada pela equação: A = ℼ r^2
'''
from math import pi

def circleArea(r):
    return pi * r ** 2

r = float(input('Informe o raio do círculo: '))
print(f'A área do círculo é: {circleArea(r):.2f}')