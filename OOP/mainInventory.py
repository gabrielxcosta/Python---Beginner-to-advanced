'''
Utilizando o módulo "packInventário" para extrair os dados do arquivo
"inventory.csv" 
'''
from packInventory import Inventory, Product

print('\t\t\t    INVENTORY')
print()

print('CSV:')
Inventario = Inventory()
Inventario.read_CSV(r'C:\Users\55119\Documents\Estudos\Python\POO\inventory.csv')
Inventario.show_CSV()

print()
print('PRODUCTS:\n', '\t\t', end='')

Inventario.insert_products()
Inventario.show_products()