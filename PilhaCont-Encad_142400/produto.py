class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return 'name: ' + str(self.name) + ' price: ' + str(self.price)

    def __str__(self):
        return 'Nome: ' + str(self.name) + ' price: ' + str(self.price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name
