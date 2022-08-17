'''
Gerenciadores de contexto
'''
from contextlib import contextmanager

class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo...')
        self._arquivo = open(arquivo, modo)
    
    def __enter__(self):
        print('Retornando arquivo...')
        return self._arquivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo...')
        self._arquivo.close()

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

print()
# Outra maneira de fazer um gerenciador de contextos

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo...')
        yield arquivo
    finally:
        print('Fechando arquivo...')
        arquivo.close()

with abrir('def.txt', 'w') as arquivo:
    for i in range(1, 201):
        arquivo.write(f'Linha {i}\n')