import copy

'''
Dicionários
'''
d1 = {
    'chave1' : 'borboleta',
    'chave2' : 'sorvete',
    'chave3' : 'caramelo',
    'chave4' : 'cachorro'
    }

# Adicionando duas noves chaves de maneira diferente
d1['nova_chave'] = 'camelo'
d1.update({(1, 2, 3, 4) : 'tupla'})

print('Dicionário:', d1, '\n')

# Fazendo verificações dentro do dicionário:

print("\nO dicionário contem alguma chave entitulada 'chave1'?", 'chave1' in d1)
print("O dicionário contem o valor 'caramelo' associado a alguma chave?", 'caramelo' in d1.values())
print()

# Desempacotando o dicionário em um loop:
for key, values in d1.items():
    print(key, values)
print()

# Criando um novo dicionário que aponta para o dicionário original
novo_dic = d1
print('O endereço de memória do dic novo é o mesmo do dic original?', id(d1) == id(novo_dic))
print()

d1['usuário'] = ['Gabriel', 'Larissa']

# Fazendo uma cópia rasa (em uma nova variável) do dicionário original 
n_dic = d1.copy()
print('O endereço de memória do dic cópia rasa é o mesmo do dic original?', id(d1) == id(n_dic))
n_dic['usuário'][0] = 'João'
print()
print('Dic original:', d1, '\n')
print('Dic cópia rasa:', n_dic, '\n')

# Fazendo uma cópia profunda (em uma nova variável) do dicionário original
n_dic2 = copy.deepcopy(d1)
print('O endereço de memória do dic cópia profunda é o mesmo do dic original?', id(d1) == id(n_dic2))
n_dic2['usuário'][0] = 'Marcelo'
print()
print('Dic original:', d1, '\n')
print('Dic cópia profunda:', n_dic2, '\n')

# Eliminando algum par de chaves-valores do meu dicionário original
d1.pop('chave2')
print('\n', d1)

# Eliminando o último par de chaves-valores do meu dicionário original
d1.popitem()
print('\n', d1)
