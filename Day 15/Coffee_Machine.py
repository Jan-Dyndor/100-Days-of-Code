MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(money):
    """Finction will return current resources state"""
    return print(
        f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffe: {resources['coffee']}\n Money: {money}"
    )


def off():
    """Function ends program"""
    quit()


def check_resources():
    """Function will check current resources satete and return it in varaibles"""
    water = resources["water"]
    milk = resources["milk"]
    coffe = resources["coffee"]
    return water, milk, coffe


def make_drink(drink):
    """Function will do drink if we have enought resources will return true"""
    water_res, milk_res, coffe_res = check_resources()
    if drink == "espresso":
        water_drink, coffe_drink = drink_ingredients(drink)
        water_left = water_res - water_drink
        coffe_left = coffe_res - coffe_drink
        if water_left >= 0:
            resources["water"] = water_left
            if coffe_left >= 0:
                resources["coffee"] = coffe_left
                return True
            else:
                print("Sorry there is not enough coffe")
                return False
        else:
            print("Sorry there is not enough water XXXX")
            return False
    else:
        water_drink, milk_drink, coffe_drink = drink_ingredients(drink)
        water_left = water_res - water_drink
        coffe_left = coffe_res - coffe_drink
        milk_left = milk_res - milk_drink
        if water_left >= 0:
            resources["water"] = water_left
            if coffe_left >= 0:
                resources["coffee"] = coffe_left
                if milk_left >= 0:
                    resources["milk"] = milk_left
                    return True
                else:
                    print("Sorry there is not enough milk")
                    return False

            else:
                print("Sorry there is not enough coffe")
                return False

        else:
            print("Sorry there is not enough water")
            return False


def drink_ingredients(drink):
    """Function  returns ingredients for drink"""
    wat = MENU[drink]["ingredients"]["water"]
    coff = MENU[drink]["ingredients"]["coffee"]
    if drink == "espresso":
        return wat, coff
    mil = MENU[drink]["ingredients"]["milk"]
    return wat, mil, coff


def coins():
    """Function takes drink as parameter and will ask user to insert coins, return amount"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    return money


def check_price_of_drink(drink):
    """Function returns price of drink. Takes drink as parameter"""
    price = MENU[drink]["cost"]
    return price


def can_buy(money, drink):
    """Function takes whole amonut of coins and drink name. Checks if user can buy drink. Returns true or false"""
    price = check_price_of_drink(drink)
    if money >= price:
        money -= price
        return money
    else:
        return False


money = 0
can_order = True
while can_order:
    coffe = input("What would you like? (espresso/latte/cappuccino): ")
    if coffe == "report":
        report(money)
    elif coffe == "off":
        off()
    else:
        if make_drink(coffe):
            # We have ingredients to make a coffee
            user_coins = coins()
            if can_buy(user_coins, coffe):
                # We can buy drink
                money += check_price_of_drink(coffe)
                change = can_buy(user_coins, coffe)
                print(f"Here is ${change} in change")
                print(f"Here is your {coffe}")

            else:
                print("Sorry that's not enough money. Money refunded")
