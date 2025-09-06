class my_private_info :
    __privateVar = 453789
    def __privemeth(self):
        print("my name is ditya !!!")
    def hello(self):
        print("private variable value :",my_private_info.__privateVar)
obj = my_private_info()
obj.hello()
obj.__privemeth()