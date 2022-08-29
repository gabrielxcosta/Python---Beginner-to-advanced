'''
Trabalhando com planilhas do excel usando
o módulo openpyxl
'''
import openpyxl

path = r'C:\Users\55119\Documents\Estudos\Python\Módulos\Openpyxl\pedidos.xlsx'
requests = openpyxl.load_workbook(path)
spreadsheet_name = requests.sheetnames
spreadsheet = requests['Página1']

# Exibindo os elementos da nossa planilha de pedidos
for line in spreadsheet['A1:C4']:
    for column in line:
        print(column.value, '\t', end=' ')
    print()

spreadsheet['B3'].value = 2200
requests.save('New_spreadsheet.xlsx')