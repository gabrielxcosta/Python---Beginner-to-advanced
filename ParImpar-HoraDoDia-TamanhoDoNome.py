# Exercício 1
print(50 * '-')
print(17 * ' ', 'Exercício 1')
print(50 * '-')
nro = input('Informe o número: ')
if nro.isdigit() == True:
    nro = int(nro)
    if nro % 2 == 0:
        print(f'O número {nro} é par!')
    else:
        print(f'O número {nro} é impar!')
else:
    print('O dado informado não é um número inteiro!')

print()

# Exercício 2
print(50 * '-')
print(17 * ' ', 'Exercício 2')
print(50 * '-')
horas = input('Informe a hora atual: ')
if horas.isdigit() == True:
    horas = int(horas)
    if horas >= 0 and horas <= 11:
        print('Bom dia!')
    elif horas > 11 and horas <= 17:
        print('Boa tarde!')
    elif horas > 17 and horas <= 23:
        print('Boa noite!')
else:
    print('O valor inserido não corresponde a uma hora!')
print()

# Exercício 3
print(50 * '-')
print(17 * ' ', 'Exercício 3')
print(50 * '-')
nome = input('Informe seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')