def func_2():
    return 2 ** 4

def func_1(funcao):
    return funcao()

pot = func_1(func_2)
print(pot)