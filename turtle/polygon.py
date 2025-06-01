import turtle
turtle.Screen().setup(580,600)
turtle.Screen().bgcolor("red")
polygon = turtle.Turtle()
sides = 8
angle = 360/sides
for i in range(sides):
    polygon.forward(80)
    polygon.right(angle)

turtle.done()