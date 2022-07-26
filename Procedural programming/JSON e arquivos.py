'''
JSON e arquivos em Python
'''
import json

d1 = {
    'Pessoa 1' : {
        'nome' : 'Rodrigo',
        'idade' : 45
    },
    'Pessoa 2' : {
        'nome' : 'Jonas',
        'idade' : 25
    }
}

d1_json = json.dumps(d1, indent = True)

# Escrevendo no meu arquivo JSON
with open('abc.json', 'w+') as file:
    file.write(d1_json)

# Voltando o arquivo JSON a um dicionário 
with open('abc.json', 'r') as file:
    d1_json_f = file.read()
    d1_json_f = json.loads(d1_json_f)

# Percorrendo os items do dicionário
for pessoa, dados in d1_json_f.items():
    print(pessoa)
    for k, v in dados.items():
        print(f'{k} : {v}')
    print()