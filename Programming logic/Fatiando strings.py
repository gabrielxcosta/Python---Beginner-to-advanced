# Checando se uma palavra é palíndrome usando fatiamento de strings
palavra = input('Informe a palavra: ')
inversa = None

if isinstance(palavra, str) == True:
    inversa = palavra[len(palavra) : : -1]
    print(f'Palavra invertida: {inversa}')
    print(f'\nA palavra é palíndrome: {palavra == inversa}')

else:
    print('O dado informado não é uma palavra!')