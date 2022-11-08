'''
O arange() basicamente funciona como a função range() - ou seja, ela cria uma lista (nesse caso um array numpy) 
que se inicia no 0 e tem o tamanho indicado por parâmetro.

Para chamarmos essa função, usaremos numpy.arange(), passando como valor o número 10. Como retorno, 
teremos um array de tamanho 10:
'''
import numpy as np

lista = np.arange(10)
print(lista)

print()

'''
Agora começaremos a criar propriamente os famosos arrays Numpy. Uma das maneiras de fazermos isso é a partir de uma lista. 
Para isso, criaremos uma variável km que receberá a chamada de np.array(). Passaremos como parâmetro dessa função uma lista 
contendo números aleatórios. 
'''

km = np.array([1000, 2300, 4987, 1500])
print(km)

print()

'''
Também é possível criar arrays numpy a partir de dados externos, algo que já fizemos no início desse curso. Para isso, faremos 
novamente o upload dos arquivos disponibilizados (carros-anos.txt, carros-km.txt e assim por diante). No código, criaremos 
novamente a variável km, agora recebendo a chamada de np.loadtxt().

O primeiro parâmetro que passaremos a essa função é o fname =, que receve o nome do arquivo cujo conteúdo queremos armazenar - 
nesse caso, carros-km.txt. Outro parâmetro possível é o dtype, que define o tipo de dado armazenado. O padrão na criação do 
array é float, e usaremos a instrução dtype = int para forçarmos esse tipo.
'''

km = np.loadtxt(fname='NumPy/carros-km.txt', dtype=int)
print(km)

print()

print(km.dtype)

print()

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

'''
Criaremos então uma variável Acessorios à qual atribuiremos a chamada de np.array(). Esta, por sua vez, receberá por 
parâmetro a lista dados.
'''

Acessorios = np.array(dados)

'''
É possível verificarmos a dimensão de cada um dos arrays que acabamos de criar utilizando a instrução .shape. 
Começaremos com km.shape:
'''

print(km.shape)

print()

print(Acessorios.shape)