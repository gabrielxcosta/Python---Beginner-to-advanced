'''
Em Python tudo é um objeto: incluindo classes.
Metaclasses são as classes que criam classes.
type é uma metaclasse?
'''
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'attr_classe' in namespace:
            del namespace['attr_classe']

        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método de b_fala em {name}!')
        else:
            if not callable(namespace['b_fala']):
                print(f"'b_fala' precisa ser um método, não um atributo em {name}!")
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'Valor A'
    def fala(self):
        self.b_fala()

class B(A):
    attr_classe = 'Valor B'
    def b_fala(self):
        print('Oi...tudo bem?')

class C(B):
    attr_classe = 'Valor C'

b = B()

print()

b.fala()
print()
print(b.attr_classe)

c = C()
print()
print(c.attr_classe)
print()

# Outra maneira de criar uma metaclasse

D = type(
    'D',
    (),
    {
        'attr' : 'Atributo de D'
    }
)

d = D()
print(f'Atributo de D -> {d.attr}, tipo de D -> {type(D)}')
