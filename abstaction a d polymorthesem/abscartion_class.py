from abc import ABC , abstractmethod 
class parent (ABC) :
    def print(self,x) :
        print(x)
    @abstractmethod
    def task(self):
        print("we are inside abc class")
class test (parent) :
    def task(self):
        print("we are inside test class")
poly = test()
poly.task()
poly.print(673452)