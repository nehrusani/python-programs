class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price :",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
obj = computer()
obj.sell()

obj.__maxprice =9037394
obj.sell()

obj.setmaxprice(9037394)
obj.sell()