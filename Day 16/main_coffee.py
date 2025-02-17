from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

menu = Menu()
maker=CoffeeMaker()
money=MoneyMachine()

while(True):
        choice=input(f"What would you like ? ({menu.get_items()}): ").strip().lower()
        if(choice == "report"):
             maker.report()
             money.report()
        elif choice == "off":
             sys.exit()
        elif(drink:=menu.find_drink(choice)):
            if(maker.is_resource_sufficient(drink)):
                  if(money.make_payment(drink.cost)):
                    maker.make_coffee(drink)
