'''
Métodos de classes em Python - Factory methods
'''
from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return (self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# Instanciando um objeto atráves do nome e idade 
p1 = Pessoa('João', 24)
print(f'{p1.nome} tem {p1.idade} anos. \nEle nasceu em {p1.get_ano_nascimento()}')

print()

# Instanciando um objeto atráves do nome e do ano de nascimento
p2 = Pessoa.por_ano_nascimento('Gabriel', 2001)
print(f'{p2.nome} tem {p2.idade} anos. \nEle nasceu em {p2.get_ano_nascimento()}')