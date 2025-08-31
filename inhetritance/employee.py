class person :
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display (self):
        print(self.name)
        print(self.idnumber)
class employee(person) :
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        print(self.salary)
        person.__init__(self,name,idnumber)
work = employee("Ditya saini",9089768,10000000,"astronaut")
work.display()
