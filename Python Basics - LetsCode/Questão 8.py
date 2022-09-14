'''
QUESTÃO 8

Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

Dica: Use três variáveis:
● um contador;
● uma variável para soma;
● e uma variável para os termos.

Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3!.
'''
def fat(n):
    count = 1
    if not n == 1:
        for number in range(1, n + 1):
            count *= number
        return count
    return count

sumCount = 0
for i in range(1, 1001):
    sumCount += (1 / fat(i))

print(f'A soma de mil termos dos inversos dos fatoriais é: {sumCount:.3f}')