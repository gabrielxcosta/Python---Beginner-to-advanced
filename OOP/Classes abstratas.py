'''
Classes abstratas em Python
'''
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, ag, conta, saldo):
        self._ag = ag
        self._conta = conta
        self._saldo = saldo
    
    @property
    def ag(self):
        return self._ag

    @property
    def conta(self):
        return self._conta
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser númerico!')
        
        self._saldo = valor
    
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor depositado precisa ser númerico!')
        
        self.saldo += valor
        self.resumo()
    
    def resumo(self):
        print(f'AG: {self.ag}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: R${self.saldo:.2f}')
    
    @abstractmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return
        
        self.saldo -= valor
        self.resumo()

class ContaCorrente(Conta):
    def __init__(self, ag, conta, saldo, limite=100):
        super().__init__(ag, conta, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente!')
            return
        
        self.saldo -= valor
        self.resumo()

c_poup = ContaPoupanca(1111, 2222, 0)
c_poup.depositar(10)

print()

c_poup.sacar(5)
print()
c_poup.sacar(5)
print()
c_poup.sacar(5)
print()

#######################################

c_c = ContaCorrente(ag=1111, conta=3333, saldo=0, limite=500)
c_c.depositar(100)
print()
c_c.sacar(250)
print()
c_c.sacar(500)
print()
c_c.depositar(1000)