import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t. speed(0)
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 1/n
    t.pencolor(c)