'''
Este pacote contém as classes: Pessoa (super-classe) e
Cliente (classe filha que contém uma agregação da classe Conta)
'''
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None
    
    @property
    def conta(self):
        return self._conta
    
    def inserir_conta(self, conta):
        self._conta = conta