usuario = input('Informe o nome de usuário: ')
senha = input('Informe a senha: ')

usuarios_bd = ['luiz', 'gabriel', 'vinicius', 'larissa', 'caio']
senhas_bd = ['123456', 'xuxu2712', 'necronark123', 'dirijo4i20', 'camarao123']

if usuario in usuarios_bd and senha in senhas_bd:
    print('\nVocê logou no sistema!')
else:
    print('\nUsuário e senha inválidos!')