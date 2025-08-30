import random

class Employee:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.money = 0

    def work(self):
        if self.energy >= 10:
            earned = random.randint(10, 50)
            self.money += earned
            self.energy -= 10
            print(f"{self.name} worked and earned ${earned}. Energy left: {self.energy}")
        else:
            print(f"{self.name} is too tired to work.")

    def rest(self):
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} rested. Energy is now {self.energy}.")

    def status(self):
        print(f"{self.name} | Energy: {self.energy} | Money: ${self.money}")

def main():
    name = input("Enter employee name: ")
    emp = Employee(name)

    while True:
        print("\nChoose an action:")
        print("1. Work")
        print("2. Rest")
        print("3. Status")
        print("4. Quit")
        choice = input("Your choice: ")

        if choice == "1":
            emp.work()
        elif choice == "2":
            emp.rest()
        elif choice == "3":
            emp.status()
        elif choice == "4":
            print("Game over!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()