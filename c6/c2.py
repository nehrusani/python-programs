a = int(input("enter a number : "))
b = int(input("enter the second number : "))
class gira :
    def rtgf(self,a,b) :
        self.a = a
        self.b = b
        return a + b
    
    def subtract(self, a, b):
        self.a = a
        self.b = b
        return a - b

    obj = gira()
    print("Sum:", obj.rtgf(a, b))
    print("Difference:", obj.subtract(a, b))