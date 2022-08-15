'''
Composição entre classes
'''

class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []
    
    def insere_endereco(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))
    
    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado

cliente1 = Cliente('Marcelo', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print('Endereços do Marcelo:')
cliente1.lista_enderecos()

print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Cabo Frio', 'RJ')
print('Endereços de Maria:')
cliente2.lista_enderecos()

print()

cliente3 = Cliente('João', 23)
cliente3.insere_endereco('Guarulhos', 'SP')
print('Endereços do João:')
cliente3.lista_enderecos()