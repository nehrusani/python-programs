class namw :
    def __init__(self,number):
        self.number = number

    def __gt__(self,other) :
        return self.number > other.number
    
    def __eq__(self,other) :
        return self.number == other.number
    
ob1 = namw(4)
ob2 = namw(3)

print(ob1 > ob2)
print(ob1 == ob2)