import turtle
turtle.Screen().setup(580,600)
turtle.Screen().bgcolor("red")
turtle.title("spiral pattern")
polygon = turtle.Turtle()
sides = 4
size=0
while True:
    for i in range(sides):
        polygon.forward(size+1)
        polygon.left(90)
        size=size-5
    size=size+1    
turtle.done()