class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Qty: {self.quantity}"

class Smartphone(Product):
    def __init__(self, name, price, quantity, os):
        super().__init__(name, price, quantity)
        self.os = os

    def __str__(self):
        return f"Smartphone: {self.name} ({self.os}), Price: {self.price}"

class Laptop(Product):
    def __init__(self, name, price, quantity, ram):
        super().__init__(name, price, quantity)
        self.ram = ram

    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram
        print(f"RAM upgraded to {self.ram}GB")
