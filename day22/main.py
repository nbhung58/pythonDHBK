from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#screen
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong game")

#paddle setup position
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)



#move paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down") 
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s") 

#ball
ball = Ball()
scoreboard = ScoreBoard()
a = 0.1

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.y_bounce()

    #Detect collistion with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        print("Make contact")
    
    #detect R missing and L missing
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
       # a /= 100
    
    #detect L missing
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
       # a /= 100



screen.exitonclick()