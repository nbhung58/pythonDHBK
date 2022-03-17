import turtle as t
from random import choice, randint

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

tim.speed(0.1)
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading +10)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()


