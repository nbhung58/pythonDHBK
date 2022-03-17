from turtle import Turtle

class Ball(Turtle):
    def __init__(self) :
        super().__init__()    
        self.shape("circle")
        self.penup() #endup drawing
        #self.shapesize(stretch_len= 0.7, stretch_wid= 0.7)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def y_bounce(self):
        self.y_move *= -1
        #self.move_speed *= 0.5
        
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.5
    
    def reset_position(self):
        #self.penup()
        self.goto(0,0)
        self.x_bounce()
        

