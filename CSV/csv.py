class csv :
    def __init__(self,name,age,business):
        self.name = name
        self.age = age
        self.business = business
    
    def declear(self,name,age,business):
        if name == " " or name == "":
            print("invalid input")
            return
        elif age == " " or age == "":
            print("invalid")
            return
        self.name = name
        self.age = age
        self.business = business
    
    def repeat_and_display(self, times=4):
        for _ in range(times):
            self.declear(
                name=str(input("enter your name :")),
                age=int(input("enter your age :")),
                business=str(input("enter your business :"))
            )
        print(f"{self.name}, {self.age}, {self.business}")
obj = csv("", 0, "")
obj.declear(name=str(input("enter your name :")),age = int(input("enter your age :")),business=str(input("enter your business : ")))
print(f"\n{obj.name}\n{obj.age}\n{obj.business}")