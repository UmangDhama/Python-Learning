from idlelib.mainmenu import menudefs

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def CoffeeMachine():
    is_on=True


    while is_on:

        drink=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink=="off":
            is_on=False
            continue

        elif drink=="report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            continue
        if drink not in MENU:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")
            continue
        drink_milk_amount=0
        if drink=="espresso":
            drink_water_amount=MENU[drink]["ingredients"]["water"]
            drink_coffe_amount=MENU[drink]["ingredients"]["coffee"]
        else:
            drink_milk_amount = MENU[drink]["ingredients"]["milk"]
            drink_water_amount = MENU[drink]["ingredients"]["water"]
            drink_coffe_amount = MENU[drink]["ingredients"]["coffee"]
        if drink=="espresso":
            if drink_water_amount>resources["water"]:
                print("Sorry there is not enough water.")
                continue
            elif drink_coffe_amount>resources["coffee"]:
                print("Sorry there is not enough coffee.")
                continue
        else:
            if drink_water_amount>resources["water"]:
                print("Sorry there is not enough water.")
                continue
            elif drink_coffe_amount>resources["coffee"]:
                print("Sorry there is not enough coffee.")
                continue
            elif drink_milk_amount>resources["milk"]:
                 print("Sorry there is not enough milk.")
                 continue


        drink_cost=MENU[drink]["cost"]
        print(drink_water_amount)
        print(drink_coffe_amount)
        print(drink_cost)
        print("Please insert coins.")

        quarters=float(input("how many quarters?: "))
        dimes=float(input("how many dimes?: "))
        nickles=float(input("how many nickels?: "))
        pennies=float(input("how many pennies?: "))
        total=(0.24*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)

        if total<drink_cost:
            print("Sorry that's not enough money. Money refunded.")

        else:
             print(f"Here is ${total-drink_cost} in change.")
             print(f"Here is your {drink}☕️. Enjoy!")
             resources["water"]-=drink_water_amount
             resources["milk"]-=drink_milk_amount
             resources["coffee"]-=drink_coffe_amount

CoffeeMachine()