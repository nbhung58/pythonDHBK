
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ") 
    if choice == "off":
        is_on = False
    elif choice == "report":    #1. print report    
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #2 Check resources sufficient 3 Check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            #3Process coins
                #5make coffee
                coffee_maker.make_coffee(drink)

