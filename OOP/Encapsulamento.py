'''
Encapsulamento em Python

_ private/protected - 1 underline
__ private - 2 underlines
'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    def insere_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else:
            self.__dados['clientes'].update({id : nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

base_dados = BaseDeDados()
base_dados.insere_cliente(1, 'Gabriel')
base_dados.insere_cliente(2, 'João')
base_dados.insere_cliente(3, 'Maria')

print('Clientes:')
base_dados.lista_clientes()

# Deletando um cliente do nosso dicionário
base_dados.apaga_cliente(2)
print('\nClientes após a remoção:')
base_dados.lista_clientes()

print()

print(base_dados._BaseDeDados__dados)
print(base_dados.dados)