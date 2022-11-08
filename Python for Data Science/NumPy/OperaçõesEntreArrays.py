import numpy as np
from datetime import datetime

# To ignore the warning of division by zero:
# The elements of the respective indices will be filled with NaN
np.seterr(invalid='ignore')

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
currentYear = datetime.now().year

idade = currentYear - anos
km_media = km / idade
print('Km média:', km_media)

dados = np.array([km, anos])
print('Tamanho do array:', dados.shape)

print()

print('Km:', dados[0])
print('Anos:', dados[1])

km_media = dados[0] / (2019 - dados[1])