'''
QUESTÃO 6

Faça uma função que recebe uma lista de números e retorna 
a soma dos elementos dessa lista.
'''
def sumList(nList):
    count = 0
    for value in nList:
        count += value
    return count

list1 = [x for x in range(1, 11)]
print(f'A soma da lista é: {sumList(list1)}')