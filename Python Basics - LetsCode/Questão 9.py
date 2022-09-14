'''
QUESTÃO 9

Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
    1. uma lista com os 4 primeiros números;
    2. uma lista com os 5 últimos números;
    3. uma lista contendo apenas os elementos das posições pares;
    4. uma lista contendo apenas os elementos das posições ímpares;
'''

list1 = [x for x in range(1, 11)]
print(f'Lista original: {list1}')

print()

# 1.
print('1.', list1[ : 4])

# 2.
print('2.', list1[5 : ])

# 3.
evens = [x for x in list1 if x % 2 == 0]
print('3.', evens)

# 4.
odds = [x for x in list1 if x % 2 != 0]
print('4.', odds)