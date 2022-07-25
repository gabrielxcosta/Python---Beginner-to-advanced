'''
Tratando exceções em Python com Try, Except
'''

# Exemplo 1
print('\tExemplo 1:')
try:
    a = 1 / 0
except ZeroDivisionError as erro:
    print('Opa, divisão por zero!')
except NameError as erro:
    print('ErrorName...')
except (IndexError, KeyError) as erro:
    print('IndexError/KeyError...')
except Exception as erro:
    print('Exception')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente!')

print()

# Exemplo 2
print('\tExemplo 2:')
try:
    b = {}
    print(b['chave'])
except ZeroDivisionError as erro:
    print('Opa, divisão por zero!')
except NameError as erro:
    print('ErrorName...')
except (IndexError, KeyError) as erro:
    print('IndexError/KeyError...')
except Exception as erro:
    print('Exception')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente!')

print()

# Exemplo 3
print('\tExemplo 3:')
try:
    print(c)
except ZeroDivisionError as erro:
    print('Opa, divisão por zero!')
except NameError as erro:
    print('ErrorName...')
except (IndexError, KeyError) as erro:
    print('IndexError/KeyError...')
except Exception as erro:
    print('Exception')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente!')