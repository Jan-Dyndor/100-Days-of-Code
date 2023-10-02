from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money = MoneyMachine()

should_continue = True
while should_continue:
    print("What would you like to drink?")
    print(menu.get_items())
    drink = input()
    if drink == "off":
        should_continue = False
    elif drink == "report":
        coffe_maker.report()
        money.report()
    else:
        drink_object = menu.find_drink(drink)
        if drink_object is not None and coffe_maker.is_resource_sufficient(drink_object):
            if money.make_payment(drink_object.cost):
                coffe_maker.make_coffee(drink_object)











