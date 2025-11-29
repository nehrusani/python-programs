class Me:
    def __init__(self, name, birth, hobbie):
        self.name = name 
        self.birth = birth
        self.hobbie = hobbie

    def india(self):
        return self.name, self.birth, self.hobbie


# Example usage:
person = Me("Rahul", 1998, "Cricket")
print(person.india())  # ('Rahul', 1998, 'Cricket')