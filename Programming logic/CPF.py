'''
Verificando a validade de um CPF
'''

cpf = input("Informe o CPF (com pontos '.' e traço '-'): ")
valores_sep = cpf.split('-') # Separando o CPF em uma lista com os 9 primeiros dígitos
valores_sep_2 = valores_sep[0].split('.') # Separando os 9 primeiros dígitos em uma lista de 3 em 3
digitos_calculo = ''.join(valores_sep_2) # Juntando a lista dos 9 primeiros dígitos em uma string
novo_cpf = digitos_calculo
aux_cpf = digitos_calculo + valores_sep[1]

soma_aux = 0 # Variável para auxiliar na soma verificadora 
for i, j in enumerate(range(10, 1, -1)):
    aux_dig = None
    aux_dig = int(digitos_calculo[i]) # Cast de cada dígito
    soma_aux += (aux_dig * j)

# Verificando o primeiro dígito de valores_sep[1]
res = (soma_aux % 11)
if res >= 10: 
    res = '0'
else:
    res = str(11 - res)

if valores_sep[1][0] != res: # Checando a equivalência do primeiro dígito verificador
    print('CPF inválido!')
    quit()

novo_cpf += res # Concatenando as strings

soma_aux = 0 # Variável para auxiliar na soma verificadora 
for i, j in enumerate(range(11, 1, -1)):
    aux_dig = None
    aux_dig = int(novo_cpf[i]) # Cast de cada dígito
    soma_aux += (aux_dig * j)

# Verificando o segundo dígito de valores_sep[1]
res = (soma_aux % 11)
if res >= 10: 
    res = '0'
else:
    res = str(11 - res)

if valores_sep[1][1] != res: # Checando a equivalência do primeiro dígito verificador
    print('CPF inválido!')
    quit()

novo_cpf += res # Concatenando as strings

if aux_cpf == novo_cpf: # Última verificação
    print('CPF válido!')