class vehicle :
    def __init__(self,max_speed,mileage):
        self.max_speed= max_speed
        self.mileage=mileage
ob = vehicle(110,100)
print(ob.max_speed,"this is the car speed!!!")
print(ob.mileage,"this is the mileage of the car!!!")