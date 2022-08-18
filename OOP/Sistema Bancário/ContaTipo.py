'''
Este pacote contém as classes: Conta (super-classe),
ContaCorrente (classe filha) e Conta Poupanca (classe filha)
'''
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, ag, nconta, saldo):
        self._ag = ag
        self._nconta = nconta
        self._saldo = saldo
    
    @property
    def ag(self):
        return self._ag
    
    @property
    def nconta(self):
        return self._nconta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser númerico!')
        
        self._saldo = valor

    def resumo(self):
        print('\tRESUMO DA CONTA\n')
        print(f'AG: {self._ag}')
        print(f'Nro da conta: {self._nconta}')
        print(f'Saldo atual: R${self._saldo:.2f}')
    
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor depositado precisa ser númerico!')
        
        self.saldo += valor
        
        print('\tCOMPROVANTE DE DEPÓSITO\n')
        print(f'Valor depositado: R${valor:.2f}')
        print(f'AG: {self._ag}')
        print(f'Nro da conta: {self._nconta}')
        print(f'Saldo atual: R${self._saldo:.2f}')

    @abstractmethod
    def sacar(self, valor): pass

class ContaCorrente(Conta):
    def __init__(self, ag, nconta, saldo, limite):
        super().__init__(ag, nconta, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saque indisponível: saldo insuficiente!')
            return

        self.saldo -= valor
        print(f'Saque de R${valor:.2f} realizado!\n')
        self.resumo()

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saque indisponível: saldo insuficiente!')
            return
        
        print(f'Saque de R${valor:.2f} realizado!\n')
        self.saldo -= valor
        self.resumo()