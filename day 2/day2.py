# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
print(age)
left= 90 - age
days = left*365
weeks = days/7
months = left*12
print("You have "+ str(days)  + " days, "+ str(int(weeks)) + " weeks, "+ str(months) +" month! ")
