'''
Funções decoradoras e decoradores em Python
'''

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada!')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi():
    print('Oi!')

@master
def outra_funcao(msg):
    print(msg)

fala_oi()
print()
outra_funcao('Oi, eu sou Gabriel')
