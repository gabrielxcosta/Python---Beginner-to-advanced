from turtle import setx


print(50 * '-')
print(17 * ' ', 'Jogo da forca')
print(50 * '-')
print()

secreto = 'perfume'
print(len(secreto) * '_', end=' ')
print(f'-> {len(secreto)} letras')
digitadas = []
tentativas = 0
acabou = True
print()

while acabou and tentativas < 3:
    letra = input('Informe uma letra: ')
    if len(letra) > 1 or letra.isdigit() == True:
        print('Valor inválido!')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f"A letra '{letra}' existe na palavra!")
    else:
        print(f"A letra '{letra}' não existe na palavra!")
        digitadas.pop()
        tentativas += 1
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '_'
    if '_' not in secreto_temp:
        acabou = False
    print(secreto_temp, '\n')

