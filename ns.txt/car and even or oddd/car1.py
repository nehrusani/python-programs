from car import Car

max_speed = int(input("Enter the maximum allowed speed: "))
current_speed = int(input("Enter the car's current speed: "))

my_car = Car(current_speed, max_speed)
my_car.check_speed()
