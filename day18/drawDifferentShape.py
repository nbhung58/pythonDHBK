from turtle import Turtle
from random import choice
num_sides = 12
angle = 360/(num_sides)
shape = Turtle()
color = ["cyan", "dark goldenrod", "dark khaki", "red", "crimson"]

for i in range(3,num_sides):
    angle = 360/(i)
    shape.color(choice(color))
    for line in range(i): 
        shape.forward(100)
        shape.right(angle)


       