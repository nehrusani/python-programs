class parrot :
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob = parrot("mia",9)
ob1= parrot("lia",8)
print(ob.name,"is a",ob.species,"is",ob.age,"years old")
print(ob1.name,"is a",ob1.species,"is",ob1.age,"years old")