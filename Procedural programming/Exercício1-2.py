'''
Exercício 1 - Compreensão de lista
'''
string = '01234567890123456789012345678901234567890123456789'
print('String original:', string)
comp = [string[i : i + 10] for i in range(0, len(string), 10)]
print('Lista com as strings separadas:', comp)
comp = '.'.join(comp)
print('String unida por pontos:', comp)
