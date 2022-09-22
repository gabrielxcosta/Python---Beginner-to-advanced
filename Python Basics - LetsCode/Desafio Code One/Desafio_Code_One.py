'''
Resolvendo o Desafio_Code_One:
'''

import random
import sys
import os

def palavraSecreta(path):
    palavra = None
    with open(fr'{path}', 'r') as file:
        palavra = random.choice(list(file))
        while "'" in palavra or '-' in palavra:
            palavra = random.choice(list(file))
    tam = len(palavra)
    return palavra.lower()[ : tam - 1 : ]

def showMenu():
    print('1. Jogar...')
    print('2. Ver as intruções...')
    print('3. Sair...')

path = r'C:\Users\55119\Documents\Estudos\Python\Python Basics - LetsCode\Lista-de-Palavras.txt'
partidas = True
aux = 0
auxPartidas = []

print(50 * '-')
print(17 * ' ', 'JOGO DA FORCA')
print(50 * '-')
print()

player = input('Informe o seu nome: ')

print()
print(f'\tBem vindo {player.lower()}!')

if not isinstance(player, str):
    raise TypeError('Player precisa ser uma string!...')

while partidas:
    if aux > 0:
        os.system('cls')
        if auxPartidas[-1]:
            print('Parabéns, você ganhou!...') 
        print('Vamos jogar de novo?...')
        print()

    showMenu()

    try:
        opcao = int(input('Informe a opção: '))
    except:
        raise ValueError('Opção precisa ser um número inteiro!...')

    if opcao == 1:
        secreto = palavraSecreta(path)
        print(len(secreto) * '_', end=' ')
        print(f'-> {len(secreto)} letras')
        digitadas = []
        tentativas = 0
        acabou = True
        print()

        while acabou and tentativas < 6:
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

                if tentativas == 6:
                    auxPartidas.append(False)

            secreto_temp = ''
            for letra_secreta in secreto:
                if letra_secreta in digitadas:
                    secreto_temp += letra_secreta
                else:
                    secreto_temp += '_'
            if '_' not in secreto_temp:
                acabou = False
                auxPartidas.append(True)
            print('Palavra:', secreto_temp, '\n')
            aux += 1

    if opcao == 2:
        print()
        print(
            'O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras e o tema ligado à palavra. A cada letra errada, é desenhado uma parte do corpo do enforcado. O jogo termina ou com o acerto da palavra ou com o término do preenchimento das partes corpóreas do enforcado.',
            'Para começar o jogo se desenha uma base e um risco correspondente ao lugar de cada letra.',
            'Por exemplo, para a palavra "MERCADO", se escreve:',
            '\n\tMERCADO ------> _ _ _ _ _ _ _\n',
            'O jogador que tenta adivinhar a palavra deve ir dizendo as letras que podem existir na palavra. Cada letra que ele acerta é escrita no espaço correspondente.',
            '\n\tMERCADO → M _ _ C A _ _\n' 
            )
        print()

    if opcao == 3:
        sys.exit()