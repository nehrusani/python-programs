import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)

class Sprite(turtle.Turtle) :
    def __init__(self,spriteshape,color,startx,starty) :
        turtle.Turtle.__init__(self,shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)

        self.speed = 1
player = Sprite("triangle", "white", 0, 0)
delay = input("press enter to finish. > ")