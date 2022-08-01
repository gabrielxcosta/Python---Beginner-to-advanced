'''
Getters e setters de classes em Python

SETTER = CONFIGURANDO UM VALOR (=)
GETTER = OBTER UM VALOR (.)
'''
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

print('Usando o getter:')
p1 = Pessoa('Gabriel')
print(p1.nome)

print()

print('Usando o setter:')
p1.nome = 'João'
print(p1.nome)