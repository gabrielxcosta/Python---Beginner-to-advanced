'''
Tempo de execução de um programa com funções decoradoras e decoradores em Python
'''
from time import time, sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000 # ms
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i + 1)
        sleep(1)

demora()