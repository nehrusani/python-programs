class bus :
    def __init__(self,mileage,company):
        self.mileage=mileage
        self.company = company
class vehicel(bus):
    pass
start = bus(16,"volvo")
print(start.mileage)
print(start.company)