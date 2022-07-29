import PackCNPJ

print(30 * '-', '\n\tValidando CNPJ\n', 30 * '-', sep = '')

CNPJ = input('Informe o CNPJ (com /, . e -): ')
print(f'O CNPJ {CNPJ} é', PackCNPJ.executa_validacao(CNPJ))