from art import logo
import random

#Compare Guess_number 
def check_answer(guess_number,random_number):
  if guess_number > random_number:
    print("Too high\nGuess again!")
  elif guess_number < random_number:
    print("Too low\nGuess again!")
    
  elif guess_number == random_number:
    game_is_over = True
    print(f"You got it! The answer was {random_number}")
    return game_is_over
def check_mode(difficulty):
  if difficulty == "hard":
    return 5
  elif difficulty == "easy":
    return 10
#Start game
def game():
  print(logo)
  easy_type = 10
  hard_type = 5
  print("Welcome to the Number Guessing Game")
  print("I'm thingking of a number between 1 and 100.")
  
  #random number
  random_number = random.randint(1,100)
  #print(f"Pesst, the correct answer is {random_number}")
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if mode == "easy":
      print(f"You have {easy_type} attempts remaining to guess the number")
  elif mode == "hard": 
      print(f"You have {hard_type} attempts remaining to guess the number")
  game_is_over = False
  attempts = check_mode(mode)
  while not game_is_over:
    if attempts > 0:
      guess_number = int(input("Make a guess: "))  
      check_answer(guess_number, random_number)
      attempts -=1
      print(f"You have {attempts} attempts remaining to guess the number")
    else:
      print("You lose!")
      game_is_over = True
  
game()  
  


