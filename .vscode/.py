import os
import random
import turtle 
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("green")

turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
class sprite(turtle.Turtle):
  def _init_(self,spriteshape,color,startx,starty) :
    turtle.Tuetle._init_(self,shpe = spriteshape)
    self.speed(0)
    self.penup()
    self.color(color)
    self.fd(0)
    self.goto(startx,starty)
    self.speed = 0

delay =input("press enter to finsh. >")