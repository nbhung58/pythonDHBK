#Day 5 start
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit+ " Pie")

#Tổng từ 1 đến n
total = 0
for number in range(1,101):
  total += number
print(total)

#Day 5-1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  


#Write your code below this row 👇
total_height = 0
total_student = 0
for student_height in student_heights:
  total_height = total_height + student_height
  total_student+=1

# total_student = n + 1
average = int(total_height/total_student)
print(average)

#5-2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"the highest score is {highest_score}")

#5-3
#Write your code below this row 👇 Tính tổng theo số chẵn/lẻ
total = 0
for i in range(1,101):
  if i%2 == 0:
    total += i
  
print(total)

#5-4 FizzBuzz
#Write your code below this row 👇
for number in range(1,101):
  if number%3 ==0 and number%5 == 0:
    print("FizzBuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("buzz")
  else:
    print(number)

#END: Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(0,nr_letters):
  letter = random.choice(letters)
  password = password + letter
for j in range(0, nr_symbols):
  symbol = random.choice(symbols)
  password = password + symbol
for x in range(0, nr_numbers):
  number = random.choice(numbers)
  password = password + number
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for i in range(0,nr_letters):
  letter = random.choice(letters)
  password_list.append(letter)
for j in range(0, nr_symbols):
  symbol = random.choice(symbols)
  password_list.append(symbol)
for x in range(0, nr_numbers):
  number = random.choice(numbers)
  password_list.append(number)
random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is {password}")
