class vihicel :
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed= maxspeed
        self.mileage = mileage
class bus(vihicel) :
    pass
schoolbus = bus("school volvo",400,900)
print(schoolbus.name)
print(schoolbus.maxspeed)
print(schoolbus.mileage)