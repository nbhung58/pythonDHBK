from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
menu = Menu()


while is_on:
    #0 user choose the drink
    option = menu.get_items()
    choice = input(f"What would you like to drink? {option} ")
    if choice == "off":
        is_on =  False
    #1 print report
    elif choice == "report":        
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                

            