'''
Getters e setters de classes em Python - @property / @NOME.setter
'''
class Produto():
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

# Getter do preço
    @property
    def preco(self):
        return self._preco

    # Setter do preço
    @preco.setter
    def preco(self, valor):
        if type(valor) == str:
            self._preco = float(valor.replace('R$', ''))
    
    def desconto(self, percentual):
        self._preco = self._preco - (self._preco * (percentual / 100))
        return self._preco

    # Getter do nome
    @property
    def nome(self):
        return self._nome
    
    # Setter do nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()
    

p1 = Produto('CAMISETA', 20.0)
p1.preco = '50.0'

print(f'A {p1.nome} custa {p1.preco}')

p1desconto = p1.desconto(50) 
print(f'O preço da {p1.nome} com o desconto é de R${p1desconto}')