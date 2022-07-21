'''
Utilizando compreensão de listas para visualizar qtos primos há de 2 a 1000
'''
primos = [i for i in range(2, 1001) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
for index, num in enumerate(primos):
    print(f'{index}° primo:', num)