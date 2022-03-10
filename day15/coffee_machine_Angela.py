from pickle import TRUE
from coffee_machine_data import MENU, resources
from art import logo

profit = 0
def is_resource_sufficient(order_inncredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_inncredients:
        if order_inncredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True



def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins. ")
    total =  int(input("How many quarters?: "))*0.25
    total += int(input("How many dims?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, 
    or False if money insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")


#Run machine 
is_on =True
print(logo)
while is_on:
    choice = input("What would you like? (Espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:  ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


