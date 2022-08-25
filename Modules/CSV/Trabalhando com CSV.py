"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...

Usaremos o "Mall customers" dataset -> https://www.kaggle.com/datasets/shrutimechlearn/customer-data
"""
import csv

with open(r'Python\Módulos Python\CSV\Mall_Customers.csv', 'r') as file:
    dt = [x for x in csv.DictReader(file)]

    
with open('Clientes.csv', 'w+') as file:
    writer = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    keys = dt[0].keys()
    keys = list(keys)
    
    writer.writerow(key for key in keys)

    for data in dt:
        writer.writerow(
            [
                data['CustomerID'],
                data['Genre'],
                data['Age'],
                data['Annual_Income_(k$)'],
                data['Spending_Score']
            ]
        )