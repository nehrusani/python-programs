from abc import ABC, abstractmethod
class Animal(ABC) :
    def move (self):
        pass
class Human(Animal):
    def move(self):
        print("i can walke and run")
class Snake(Animal):
    def move(self):
        print("i can croll")
class dog(Animal):
    def move(self):
        print("i can bark")
obj = Human()
obj.move()
hu = Snake()
hu.move()
mu = dog()
mu.move()
