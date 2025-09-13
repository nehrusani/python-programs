class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Example usage
if __name__ == "__main__":
    car = Vehicle("Toyota", "Corolla", 2022)
    car.display_info()