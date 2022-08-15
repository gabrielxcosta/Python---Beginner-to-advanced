'''
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__nomeclasse = self.__class__.__name__

    @property
    def nome(self):
        return self.__nome

    @property
    def nomeclasse(self):
        return self.__nomeclasse

    def falar(self):
        print(f'{self.__nome} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'O {self.nomeclasse} {self.nome} está comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'O {self.nomeclasse} {self.nome} está estudando...')

c1 = Cliente('João', 32)
c1.falar()
c1.comprar()
print(c1.nomeclasse)

print()

a1 = Aluno('Paulo', 15)
a1.falar()
a1.estudar()
print(a1.nomeclasse)