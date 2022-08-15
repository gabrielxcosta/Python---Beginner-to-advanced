'''
Sobreposição de membros
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

    def falar(self):
        print(f'O {self.nomeclasse} {self.nome} está falando...')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, categoria):
        super().__init__(nome, idade)
        self.__categoria = categoria

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'O {self.nomeclasse} {self.nome} está na categoria {self.__categoria}')

class Aluno(Pessoa):
    def estudar(self):
        print(f'O {self.nomeclasse} {self.nome} está estudando...')

c1 = Cliente('João', 26)
c1.falar()

print()

c2 = ClienteVIP('Gabriel', 21, 'diamante')
c2.falar()