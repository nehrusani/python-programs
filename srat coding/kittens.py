import random

class Kitten:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - random.randint(10, 30))
        print(f"{self.name} has been fed. Hunger: {self.hunger}")

    def play(self):
        self.happiness = min(100, self.happiness + random.randint(10, 30))
        print(f"{self.name} played. Happiness: {self.happiness}")

    def status(self):
        print(f"{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}")

def main():
    name = input("Name your kitten: ")
    kitten = Kitten(name)

    while True:
        kitten.status()
        print("What would you like to do?")
        print("1. Feed kitten")
        print("2. Play with kitten")
        print("3. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            kitten.feed()
        elif choice == "2":
            kitten.play()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        # Kitten gets hungrier and less happy over time
        kitten.hunger = min(100, kitten.hunger + random.randint(5, 15))
        kitten.happiness = max(0, kitten.happiness - random.randint(5, 15))

        if kitten.hunger >= 100:
            print(f"{kitten.name} is too hungry! Game over.")
            break
        if kitten.happiness <= 0:
            print(f"{kitten.name} is too sad! Game over.")
            break

if __name__ == "__main__":
    main()