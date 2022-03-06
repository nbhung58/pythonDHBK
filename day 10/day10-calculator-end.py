from art import logo
#Calculator
#Add 
print(logo)

def add(n1, n2):
  return n1 + n2
  
#subtraction
def subtraction(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#devide
def devide(n1, n2):
  if n2 != 0:
    return n1/n2
  else:
    return(f"{n2} is not set to 0!")

#Create a dictionary named operations
operations = {
  "+": add, 
  "-": subtraction, 
  "*": multiply, 
  "/": devide
}


def calculator():
  num1 = float(input("What's the first number?: "))
  
  for choice in operations:
    print(choice)
    
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line obove: ")
    num2 = float(input("What's the second number?: "))
    math = operations[operation_symbol]
    answer = math(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation:  ")
    if continue_calculating == "y":
      num1 = answer
      # operation_symbol = input("Pick another operation: ")
      # num2 = int(input("What's the next number?: "))
      # calculation_function = operations[operation_symbol]
      # next_answer = calculation_function(num1, num2)
      # print(f"{num1} {operation_symbol} {num2} = {next_answer}")
    else:
      should_continue == False
      calculator()

calculator()
    


