'''
Implementando um iterator com classes
'''
class Iterator:
    def __init__(self):
        self.__items = []
        self.__index = 0
    
    def add(self, value):
        self.__items.append(value)
    
    def __getitem__(self, index):
        if not index > (len(self.__items) - 1):
            return self.__items[index]
        else:
            return f'Index [{index}] does not exist!...'
    
    def __setitem__(self, index, value):
        if not index > (len(self.__items) - 1):
            self.__items[index] = value
        else:
            return f'Index [{index}] does not exist!...'
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            print('Index out of range!...')
            raise StopIteration
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'
    
    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    listing = Iterator()
    listing.add('Marcelo')
    listing.add('Joana')
    
    for items in listing:
        print(items)
    
    print(listing[2])

    print(listing)
    listing[1] = 'Roberto'
    print(listing)