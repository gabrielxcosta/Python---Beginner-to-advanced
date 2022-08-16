class TaErradoError(Exception):
    pass

def Teste():
    raise TaErradoError('Errado!')

try:
    Teste()
except TaErradoError as error:
    print(f'Erro: {error}')