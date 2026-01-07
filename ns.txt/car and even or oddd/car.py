class Car:
    def __init__(self, speed, Max):
        self.speed = speed
        self.Max = Max

    def check_speed(self):
        if self.speed > self.Max:
            print("It is too much")
        else:
            print("Speed is OK")
    