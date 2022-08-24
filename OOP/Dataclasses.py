"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}'
            )
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
p2 = Pessoa('B', '3')
p3 = Pessoa('C', '4')
p4 = Pessoa('D', '6')

pessoas = [p1, p2, p3, p4]
pessoas.sort(key=lambda p: p.nome, reverse=True)

print(pessoas)
print(p1)

print()

print(asdict(p1))
print(astuple(p1))