# # import another_module
# # print(another_module.another_variable)

# from turtle import Turtle, Screen
# import turtle

# #Create new object
# timmy = Turtle()
# #Call methods
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)

# my_screen = Screen()
# #calling Attributes
# print(my_screen.canvheight)

# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "fire"])

table.align = "l"

print(table)