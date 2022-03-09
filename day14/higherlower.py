import art
from game_data import data
from random import choice
import os

#function for clear the command
def clear():
    os.system('cls') 


#get info person_A
def Info_person_A():
    person_A = choice(data)
    name_A = person_A['name']
    follower_A = person_A['follower_count']
    description_A= person_A['description']
    country_A = person_A['country']
    print(f"Compare A: {name_A}, a {description_A}, from {country_A}")
    return name_A, follower_A, description_A, country_A


#get info person_B
def Info_person_B():
    person_B = choice(data)
    name_B = person_B['name']
    follower_B = person_B['follower_count']
    description_B= person_B['description']
    country_B = person_B['country']
    print(f"Against B: {name_B}, a {description_B}, from {country_B}")
    return name_B, follower_B, description_B, country_B

#Start a game
#print the art of the game
print(art.logo)
game_is_over = False
#print person_A
person_A = Info_person_A()
#print the art 'VS' for the game
print(art.vs)
#print person_B
person_B = Info_person_B()

#create score
score = 0
while not game_is_over:
    player_guess = input("Who has more followers? Type 'A' or 'B': ")
    follower_A = person_A[1]
    follower_B = person_B[1]
    #compare 2 person followers
    if player_guess == "A":
        if follower_A > follower_B:
            score += 1      
            clear()
            print(f"You're right! Current score: {score}")
        elif follower_A < follower_B:
            print(f"Sorry, that's wrong.\nFinal score {score}")

    elif player_guess == "B":
        if follower_A > follower_B:
            clear()
            score += 1   
            print(f"You're right! Current score: {score}")
        elif follower_A < follower_B:
            print(f"Sorry, that's wrong.\nFinal score {score}")
            game_is_over = True

    

        



    
  
  

