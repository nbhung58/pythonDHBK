# import colorgram

# rgb_color= []
# #Extracts 6 colors from an imgage
# colors = colorgram.extract('image.jpg', 30)
# #print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)

import turtle as t
from random import choice

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()  



def random_color():
    color_list = [(232, 233, 236), (233, 232, 228), (235, 230, 233), (224, 233, 229), (40, 98, 148), (178, 46, 78), (205, 160, 93), 
(224, 210, 102), (137, 89, 63), (178, 165, 36), (110, 175, 208), (213, 130, 174), (228, 72, 48), (201, 74, 117), (92, 103, 188), (22, 154, 87), 
(122, 217, 208), (126, 41, 70), (95, 158, 62), (45, 190, 204), (226, 171, 187), (130, 189, 161), (213, 206, 38), (232, 171, 163), (172, 186, 222), 
(153, 208, 218), (104, 50, 38), (45, 62, 101), (44, 75, 80), (51, 61, 71)]
    color = choice(color_list)
    return color
screen = t.Screen()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
 

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random_color())
    #tim.penup()
    tim.forward(50)
    #tim.dot()
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()