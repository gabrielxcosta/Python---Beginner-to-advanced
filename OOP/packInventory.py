import pandas as pd

class Inventory:
    def __init__(self):
        self.__products = []
        self.__df = None
    
    @property
    def data_frame(self):
        return self.__df
    
    @property
    def products(self):
        return self.__products

    def read_CSV(self, path):
        self.__df = pd.read_csv(path)

    def show_CSV(self):
        print(self.__df)

    def show_products(self):
        print('ID', 6 * ' ', 'PRICE', 2 * ' ', 'QUANTITY')
        total_per_id = []
        quantity_per_id = []
        for product in self.products:
            print('\t\t', product.id, 5 * ' ', product.price, 5 * ' ', product.quantity)
            total_per_id.append(product.quantity * product.price)
            quantity_per_id.append(product.quantity)
        
        print()
        print(f'\t\tTotal in inventory: ${sum(total_per_id)}')
        print(f'\t\tQuantity of items in inventory: {sum(quantity_per_id)}')


    def insert_products(self):
        products = zip(self.__df['Product ID'], \
                    self.__df['Unit Price'],
                    self.__df['Quantity']
                    )

        self.__products = [Product(i, p, q) for (i, p, q) in products]

class Product:
    def __init__(self, id, price, quantity):
        self.__id = id
        self.__price = price
        self.__quantity = quantity
    
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity