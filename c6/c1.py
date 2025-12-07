class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def describe(self):
        return f"{self.name} has a value of {self.value}"

    def update_value(self, new_value):
        self.value = new_value


# Using the class
obj = MyClass("Example", 10)
print(obj.describe())

obj.update_value(25)
print(obj.describe())
