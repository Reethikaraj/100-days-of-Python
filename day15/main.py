from resources import MENU
from resources import resource


def make_coffee(choice):
    if choice == 'espresso' or 'latte' or 'cappuccino':
        if resource["water"] >= MENU[choice]["ingredients"]["water"] and resource["milk"] >= \
                MENU[choice]["ingredients"]["milk"] and resource["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
            resource["water"] -= MENU[choice]["ingredients"]["water"]
            resource["milk"] -= MENU[choice]["ingredients"]["milk"]
            resource["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            print(f"Your {choice} is ready! Enjoy!!")
        else:
            print("Insufficient resources. Calling technician!.")
            call_technician()

    elif choice != 'espresso' or 'latte' or 'cappuccino':
        new_choice = input("Please enter a valid input.\nWhat would you like? (espresso/latte/cappuccino): ")
        make_coffee(new_choice)

    return resource["water"], resource["milk"], resource["coffee"]


def reload_resources():
    resource["water"] = 300
    resource["milk"] = 200
    resource["coffee"] = 100


def print_resources():
    print(f'water = {resource["water"]}\nmilk =  {resource["milk"]}\ncoffee = {resource["coffee"]}')


def call_technician():
    isOn = False
    reload_resources()
    print("Reloaded resources.")
    isOn = True


isOn = True
while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    make_coffee(choice)
    if input() == 'off':
        isOn = False
        print("Turning off the machine!")
    if input() == 'print':
        print_resources()



