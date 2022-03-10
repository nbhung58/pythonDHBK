from coffee_machine_data import MENU, resources

#TODO 1: Prompt user

user_typing = input(" What would you like? (espresso/latte/cappucino): ")

ins_quarters = int(input("How many quarters?: "))
ins_dims = int(input("How many dims?: "))
ins_nickles = int(input("How many nickles?: "))
ins_pennies = int(input("How many pennies?: "))


#Turn off the machine
if user_typing == "off":
    turn_off = True

#print report
profit = 0 
def report(resources):
    water = resources['water']
    milk =  resources['milk']
    coffee = resources['coffee']
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {profit}g")
    return water, milk, coffee

report(resources)

#Function process coins
def process_coins(quarters, dims, nickles, pennies):
    quarters *= 0.25
    dims *=0.1
    nickles *= 0.05
    pennies *= 0.01
    return quarters, dims, nickles, pennies


#Function check resources sufficient
def check_resources_sufficient()

