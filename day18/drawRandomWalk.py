import turtle as t
from random import choice, randint

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.speed(0.1)

direction = [0, 90, 180, 270]
tim.pensize(15)


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(direction))
