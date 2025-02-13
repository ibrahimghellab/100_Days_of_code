import json
import sys


def main():
    money=0
    with open("menu.json") as m:
        menu=json.load(m)
    with open("ressources.json") as r:
        ressources=json.load(r)
    while(True):
        choice=input("What would you like ?: ").strip().lower()
        match choice:
            case "cappucino" | "espresso" | "latte":
                enough=True
                if ressources["water"]-menu[choice]["ingredients"]["water"]<0: 
                    print("Sorry there is not enough water")
                    enough=False
                if ressources["milk"]-menu[choice]["ingredients"]["milk"]<0 :
                    print("Sorry there is not enough milk")
                    enough=False
                if ressources["coffee"]-menu[choice]["ingredients"]["coffee"]<0:
                    print("Sorry there is not enough coffee")
                    enough=False

                if enough : 
                        quarters=int(input("How many quarters?: "))
                        dimes=int(input("How many dimes?: "))
                        nickles=int(input("How many nickles?: "))
                        pennies=int(input("How many pennies?: "))
                        sum=(0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies)
                        if  sum>=menu[choice]["cost"]:
                            ressources["water"]=ressources["water"]-menu[choice]["ingredients"]["water"]
                            ressources["milk"]=ressources["milk"]-menu[choice]["ingredients"]["milk"]
                            ressources["coffee"]=ressources["coffee"]-menu[choice]["ingredients"]["coffee"]
                            print(menu[choice]["cost"])
                            print(sum)
                            if(sum>menu[choice]["cost"]):
                                change = sum-menu[choice]["cost"]
                                print(f"Here is {round(change,2)} dollars in change.")
                            print(f"Here is your {choice}. Enjoy!")
                            money+=menu[choice]["cost"]
                        else:
                            print("Sorry that's not enough money. Money refunded")

                
            case ("report"):
                print(f"Water: {ressources["water"]}mL")
                print(f"Milk: {ressources["milk"]}mL")
                print(f"Coffee: {ressources["coffee"]}mL")
                print(f"Money: ${money}")
            case("off"):
                sys.exit()


if __name__ == "__main__" :
    main()