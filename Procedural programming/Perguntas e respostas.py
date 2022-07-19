'''
Sistema de perguntas e respostas com dicionários
'''
perguntas = {'Pergunta 1' : {
                'pergunta' : 'Qual a capital da Noruega?',
                'respostas' : {'a' : 'Oslo', 'b' : 'Estocolmo', 'c' : 'Helsínquia', 'd' : 'Reykjavik'},
                'resposta_certa' : 'a'},
            'Pergunta 2' : {
                'pergunta' : 'Qual o maior rio do mundo?',
                'respostas' : {'a' : 'Nilo', 'b' : 'Amazonas', 'c' : 'Yangtze', 'd' : 'Paraná'},
                'resposta_certa' : 'b'},
            'Pergunta 3' : {
                'pergunta' : 'Em qual ano se iniciou a segunda guerra mundial?',
                'respostas' : {'a' : '1918', 'b' : '1935', 'c' : '1939', 'd' : '1941'},
                'resposta_certa' : 'c'},
            'Pergunta 4' : {
                'pergunta' : 'Qual o maior planeta do sistema solar?',
                'respostas' : {'a' : 'Terra', 'b' : 'Vênus', 'c' : 'Urano', 'd' : 'Júpiter'},
                'resposta_certa' : 'd'},    
}

print('\tSistema de perguntas e respostas')

continua = 's'
while continua == 's':
    conta_acertos = 0
    for pk, pv in perguntas.items():
        print(f'\n{pk}: {pv["pergunta"]}')
        for rk, rv in pv['respostas'].items():
            print(f'{rk}: {rv}')
        resposta_aux = input('Informe a alternativa: ')
        if resposta_aux == pv['resposta_certa']:
            print('Parabéns, você acertou =)')
            conta_acertos += 1
        else:
            print('Você errou =(')
    print(f'\n\tVocê acertou {conta_acertos} perguntas.')
    print(f'\tSua porcentagem de acerto foi: {conta_acertos / len(perguntas) * 100}%')
    continua = input(f'\tVocê quer jogar novamente? ')
    if continua != 's':
        continua == 'f'
