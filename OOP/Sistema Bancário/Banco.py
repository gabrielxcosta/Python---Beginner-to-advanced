'''
Este pacote contém a classe Banco e seus métodos
para inserção de clientes, contas e autenticação dos mesmos
'''
class Banco:
    def __init__(self):
        self._ag = [1111, 2222, 3333]
        self._clientes = []
        self._contas = []
    
    @property
    def ag(self):
        return self._ag

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def inserir_conta(self, conta):
        self._contas.append(conta)
    
    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return None

        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.ag not in self.ag:
            return False
        
        return True