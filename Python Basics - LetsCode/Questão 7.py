'''
QUESTÃO 7

Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
euclidiana entre os pontos, utilizando a equação abaixo:

                            d = sqrt((x2 - x1)² + (y2 - y1)²)
'''
from math import sqrt

def euclidianDis(tuple1, tuple2):
    if not isinstance(tuple1, tuple) and isinstance(tuple2, tuple):
        raise TypeError('A função tem que receber duas tuplas!...')
    return sqrt((tuple2[0] - tuple1[0]) ** 2 + (tuple2[1] - tuple1[1]) ** 2)

x1 = float(input('Informe x1: '))
y1 = float(input('Informe y1: '))
tuple1 = x1, y1

print()

x2 = float(input('Informe x2: '))
y2 = float(input('Informe y2: '))
tuple2 = x2, y2

print()

print(f'A distância euclidiana é: {euclidianDis(tuple1, tuple2):.2f}')