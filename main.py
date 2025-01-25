from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
import coffee_maker
from money_machine import MoneyMachine

print("Welcome to the Coffee machine!")
in_use = True

balance = 0


def moneycount():
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickles = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

men = Menu()
coffee = CoffeeMaker()
moneyM = MoneyMachine()

while in_use:
    dec = input("What would you like? : ").lower()
    if dec in men.get_items():
        item = men.find_drink(dec)
        if coffee.is_resource_sufficient(item):
            moneyM.make_payment(item.cost)
            coffee.make_coffee(item)

    elif dec=="report":
        coffee.report()
        moneyM.report()

    elif dec=="off":
        in_use=False

    else:
        print("Enter valid input!")

