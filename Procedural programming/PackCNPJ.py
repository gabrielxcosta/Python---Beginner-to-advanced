import re
import random 

def gera():
    dig_1st = random.randint(0, 9)
    dig_2st = random.randint(0, 9)
    bloco_2st = random.randint(100, 999)
    bloco_3st = random.randint(100, 999)
    bloco_4st = '0001'
    cnpj = f'{dig_1st}{dig_2st}{bloco_2st}{bloco_3st}{bloco_4st}'
    soma = conta_1st_dig(cnpj)
    dig1 = valida_dig(soma)
    cnpj += dig1
    soma = conta_2st_dig(cnpj)
    dig2 = valida_dig(soma)
    cnpj += dig2
    return cnpj

def executa_validacao(entrada):
    entrada = substituir_caracteres(entrada)
    n_entrada = substituir_caracteres(entrada)[ : 12] # Fazendo uma cópia do CNPJ sem os dois dígitos finais
    soma = conta_1st_dig(n_entrada) # Calculando o primeiro dígito verificador
    dig_ver = valida_dig(soma) # Validando o primeiro dígito verificador
    n_entrada += dig_ver # Incluindo o primeiro dígito verificador na cópia do CNPJ
    soma = conta_2st_dig(n_entrada) # Calculando o segundo dígito verificador
    dig_ver = valida_dig(soma) # Validando o segundo dígito verificador
    n_entrada += dig_ver # Incluindo o segundo dígito verificador na cópia do CNPJ
    if entrada == n_entrada:
        return f'válido!'
    else:
        return f'inválido!'

def formata_cnpj(cnpj):
    cnpj = substituir_caracteres(cnpj)
    return f'{cnpj[ : 2]}.{cnpj[2 : 5]}.{cnpj[5 : 8]}/{cnpj[8 : 12]}-{cnpj[12 : 14]}'

def substituir_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def valida_dig(soma):
    soma = 11 - (soma % 11)
    if soma > 9:
        return '0'
    return str(soma)

def conta_1st_dig(cnpj):
    dig = cnpj[ : 12]
    lista = [i for i in range(5, 1, -1)]
    lista.extend([i for i in range(9, 1, -1)])
    soma = 0
    for index, digito in enumerate(dig):
        soma += (int(digito) * lista[index])
    return soma

def conta_2st_dig(cnpj):
    dig = cnpj[ : 13]
    lista = [i for i in range(6, 1, -1)]
    lista.extend([i for i in range(9, 1, -1)])
    soma = 0
    for index, digito in enumerate(dig):
        soma += (int(digito) * lista[index])
    return soma