#Link code: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_left1():
    turn_left()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def jump():
    move()
    turn_left1()
    turn_right()
    turn_right()
    turn_left()
#for loop
for i in range(6):
    jump()

number_of_hurdles = 6
#while loop
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

      
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
# for i in range(6):
 #  jump()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
    
    
    
            
    
    
    
    


