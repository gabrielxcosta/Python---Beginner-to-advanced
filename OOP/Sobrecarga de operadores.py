'''
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
'''
class Retangulo:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._area = x * y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def area(self):
        return self._area
    
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.area > other.area:
            return True
        else:
            return False

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2

print(f'R1 -> (x, y) = ({r1.x}, {r1.y}) -> Área: {r1.area}')
print(f'R2 -> (x, y) = ({r2.x}, {r2.y}) -> Área: {r2.area}')
print(f'R3 = R1 + R2 -> (x, y) = ({r3.x}, {r3.y}) -> Área: {r3.area}')
print(f'A área de R3 é maior do que a área de R1? {r3 > r1}')
print(f'A área de R3 é menor do que a área de R2? {r3 < r2}')
print(f'R1 é igual a R2? {r1 == r2}')
print(f'R2 é igual a R3? {r2 == r3}')