'''
Gerando e validando CPF's randomicamente
'''
from random import randint

cpf = str(randint(100000000, 999999999))

soma_aux = 0 # Variável para auxiliar na soma verificadora 
for i, j in enumerate(range(10, 1, -1)):
    aux_dig = None
    aux_dig = int(cpf[i]) # Cast de cada dígito
    soma_aux += (aux_dig * j)

# Verificando o primeiro dígito de valores_sep[1]
res = (soma_aux % 11)
if res >= 10: 
    res = '0'
else:
    res = str(11 - res)

cpf += res # Concatenando as strings

soma_aux = 0 # Variável para auxiliar na soma verificadora 
for i, j in enumerate(range(11, 1, -1)):
    aux_dig = None
    aux_dig = int(cpf[i]) # Cast de cada dígito
    soma_aux += (aux_dig * j)

# Verificando o segundo dígito de valores_sep[1]
res = (soma_aux % 11)
if res >= 10: 
    res = '0'
else:
    res = str(11 - res)

cpf += res # Concatenando as strings

print('CPF gerado:', cpf)
print('Tamanho da string:', len(cpf))