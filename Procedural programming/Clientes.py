'''
Iterando sobre um dicionário de clientes
'''
dic = {'Cliente 1' : 
            {
            'Nome': 'Gabriel',
            'Sobrenome' : 'Costa',
            'Idade' : 20,
            'Salário' : 1500     
            },
        'Cliente 2' :
            {
            'Nome': 'José',
            'Sobrenome' : 'Costa',
            'Idade' : 56,
            'Salário' : 5500
            },
        'Cliente 3' :
            {
            'Nome': 'Evair',
            'Sobrenome' : 'Félix',
            'Idade' : 25,
            'Salário' : 3000
            } 
    }

# Iterando sobre os pares chaves-valores
for clientes_k, clientes_v in dic.items():
    print(f'\n{clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}:', f'{dados_v}')