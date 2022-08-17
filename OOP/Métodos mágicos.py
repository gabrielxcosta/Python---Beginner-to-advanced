'''
Métodos mágicos
'''

class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste
    
    def __init__(self):
        print('No init...')

# Instanciando cópias que apontam para o mesmo espaço na memória
a = A()
b = A()
c = A()
print()

let = ['a', 'b', 'c']
aux = [a, b, c]

print(f'As instâncias são iguais? {a == b == c}')

for index, obj in enumerate(aux):
    print(f'Endereço de {let[index]} na memória: {id(obj)}')

class B:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):
        resultado = 1
        for i in args:
            resultado *= i
        return f"Resultado = {resultado}"

print()

a_2 = B()
variavel = a_2(1, 2, 3, 4, 5, nome='Gabriel Costa')
print(variavel)

print()

class C:
    def __init__(self):
        pass
    
    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Você não pode fazer isso!'
        else:
            self.__dict__[key] = value

c_2 = C()
c_2.nome = 'Gabriel Costa'
print(c_2.nome)