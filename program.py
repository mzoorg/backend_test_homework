class Product:
    def __init__(self, name = '', kalories = 0, group = ''):
        self.name = name
        self.kalories = kalories
        self.group = group
    
    def ShowProduct(self):
        print(f'{self.name} is {self.group} and has {self.kalories} kalories')


newpord1 = Product('Potatoe', 100, 'vegetables')

newpord1.ShowProduct()