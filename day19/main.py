from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def counter_closkwise():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

def clockwise():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward )
screen.onkey(key="a", fun=counter_closkwise )
screen.onkey(key="d", fun=clockwise )
screen.onkey(key="c", fun=clear)
screen.exitonclick()