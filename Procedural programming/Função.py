'''
Definindo funções simples
'''

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

def f(var):
    print(var)

def dumb():
    return f

print('Testando um simples retorno de uma função:')
divide = divisao(8, 2)
if divide:
    print(divide)
else:
    print('Conta inválida!')

print()

dumb()('Mensagem!')
print('Tipo de dumb() ->', type(dumb))

print()

var = dumb()
print('Tipo de var ->', type(var))
print('Endereço na memória de var:', id(var))
print('Endereço na memória de f:', id(f))
var('Imprime algo na tela!')