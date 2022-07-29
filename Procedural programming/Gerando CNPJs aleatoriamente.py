'''
Gerando CNPJs aleatórios
'''
import PackCNPJ
from time import time

def geraCNPJ():
    CNPJs = []
    for i in range(100):
        CNPJs.append(PackCNPJ.gera())
    return CNPJs

start_time = time()
lista_cnpj = geraCNPJ()
for index, CNPJ in enumerate(lista_cnpj):
        print(f'{index + 1}° CNPJ gerado: {PackCNPJ.formata_cnpj(lista_cnpj[index])}')
end_time = time()
tempo = (end_time - start_time) * 1000 # ms
print(f'O programa levou {tempo:.2f}ms para executar')