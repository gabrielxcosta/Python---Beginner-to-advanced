'''
Exibindo a data em pt-BR
'''
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

print(34 * '-')
print('\t\tHOJE')
print(34 * '-')
print()

dt = datetime.now()
mes_atual_str = dt.strftime('%B')
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y\nHoras atuais: %X')

print(formatacao)
print(f'Último dia do mês de {mes_atual_str}: {mdays[mes_atual - 1]}')
print(f'Qtos dias até o fim do mês? {mdays[mes_atual - 1] - dt.day}')