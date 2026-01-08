class Product:
    def __init__(self, name, price, categories):
        self.name = name
        self.price = price
        self.categories = categories

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Categories: {self.categories}")
        print()

    def is_in_category(self, category):
        return category in self.categories

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
