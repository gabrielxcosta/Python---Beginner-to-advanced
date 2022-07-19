def fala_oi(nome):
    return f'Oi {nome}'

def saudar(nome, saudacao):
    return f'{saudacao} {nome}'

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

executando = mestre(fala_oi, 'Gabriel')
print(executando)
executando2 = mestre(saudar, 'Gabriel', saudacao = 'Boa noite')
print(executando2)