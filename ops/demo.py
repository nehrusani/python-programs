class add_to_show :
    def __init__(self,arg1) :
        self.arg1 = arg1

    def __add__(self,other) :
        return self.arg1 + other.arg1
    

obj = int(input("enter your num : "))
hbj = int(input("enter another num : "))
if len(str(obj)) > 2 and len(str(hbj)) > 2:
    print("you have crossed the limit of number pleas enetr 2 digit number!!! ")
else:
    print(obj + hbj)