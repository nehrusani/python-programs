class IOString:
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = str(input("enter a string : "))
    def printstring(self):
        print("the result is :",self.str1.upper())
apple = IOString()
apple.getstring()
apple.printstring()