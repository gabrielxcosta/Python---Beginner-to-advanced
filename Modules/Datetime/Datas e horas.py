'''
Trabalhando com datas e horas com o módulo Datetime
'''
from datetime import datetime, timedelta

print('Data 1:')
data = datetime(2022, 8, 24, 22, 7)
print(data.strftime('%d/%m/%Y - %H:%M:%S'))

print()

print('Data 2:')
data_2 = datetime.strptime('20/04/2022', '%d/%m/%Y')
print(data_2.strftime('%d/%m/%Y - %H:%M:%S'))
print(f'Timestamp: {data_2.timestamp()}s')

print()

print('Data 3:')
data_3 = datetime.strptime('27/12/2001 20:00:00', '%d/%m/%Y %H:%M:%S')
data_3 = data_3 + timedelta(days=5, seconds=59*60)
print(data_3.strftime('%d/%m/%Y - %H:%M:%S'))

print()

dif_1 = data - data_2
print('Diferença de tempo entre a data 1 e data 2:')
print(f'{dif_1.days} dias')
print(f'{dif_1.total_seconds()} segundos')
print(f'A data 1 é maior que a data 2? {data > data_2}')