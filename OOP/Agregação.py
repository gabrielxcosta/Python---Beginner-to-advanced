'''
Agregação entre classes
'''

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos
    
    def insere_produto(self, produto):
        self.__produtos.append(produto)
    
    def lista_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)
    
    def total_compra(self):
        lista_aux = [produto.valor for produto in self.__produtos]
        soma = sum(lista_aux)
        return soma

class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor

print('\t CARRINHO DE COMPRAS')

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50.0)
p2 = Produto('Iphone', 10000.0)
p3 = Produto('Caneca', 15.0)

carrinho.insere_produto(p1)
carrinho.insere_produto(p2)
carrinho.insere_produto(p3)

carrinho.lista_produtos()

print()

print('TOTAL DA COMPRA', f'R${carrinho.total_compra()}')