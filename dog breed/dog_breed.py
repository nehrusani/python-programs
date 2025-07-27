class dog :
    species = "buldog"
    def __init__(self,age):
        self.age = age 
od = dog(8)
od1 = dog(7)
print(od.species,"this is the species of lino")
print(od.age,"this is the age of lino")
print(od1.species,"this is the species of lina")
print(od1.age,"this is the age of lina")