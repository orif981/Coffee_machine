def coffee_machine():
    """this is a coffee machine function.
    you can choose between 3 types of coffee: espresso,latte and cappuccino.
    first, the func checks if there are enough ingredients to make the coffee, and them checks if the user enter the
     required amount of money(and return change if the coins value entered are above the coffee's price).
      if the 2 conditions are true, the func give you the coffee.
      note: if you want to "turn off" the machine just enter "off" as an input when the machine ask you what coffee do
       you want"""
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
    my_ingredients= {"water":300,"milk":200,"coffee":100}
    flag=True
    can_make=True
    while flag:
        sum_money=0
        coffee=input("What would you want?(espresso/latte/cappuccino):\n").lower()
        if coffee=="off":
            flag=False
            break
        try:
            for item in my_ingredients:
                if coffee != "espresso":
                    if my_ingredients["water"] >= MENU[coffee]["ingredients"]["water"]:
                        if my_ingredients["milk"] >= MENU[coffee]["ingredients"]["milk"]:
                            if my_ingredients["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
                                my_ingredients["water"]-=MENU[coffee]["ingredients"]["water"]
                                my_ingredients["milk"]-=MENU[coffee]["ingredients"]["milk"]
                                my_ingredients["coffee"]-=MENU[coffee]["ingredients"]["coffee"]
                                can_make = True
                                break
                    can_make, flag = False, False
                    print("Sorry, there are not enough ingredients")
                    break
                else:
                    if my_ingredients["water"] >= MENU[coffee]["ingredients"]["water"]:
                        if my_ingredients["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
                            my_ingredients["water"] -= MENU[coffee]["ingredients"]["water"]
                            my_ingredients["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
                            can_make = True
                            break
                    can_make,flag = False,False
                    print("Sorry, there are not enough ingredients")
                    break
            if can_make:
                print("Please insert coins")
                num_quarters=int(input("How many quarters?: "))
                num_dimes = int(input("How many dimes?: "))
                num_nickles = int(input("How many nickles?: "))
                num_pennies = int(input("How many pennies?: "))
                sum_money=num_quarters*0.25+num_dimes*0.1+num_nickles*0.05+num_pennies*0.1**2
                if sum_money<MENU[coffee]["cost"]: print("Sorry,that's not enough money. Money refunded.")
                elif sum_money==MENU[coffee]["cost"]:
                    print("Here is your {}, Enjoy!".format(coffee))
                else:
                    print("Here is ${} in change".format(round(sum_money-MENU[coffee]["cost"],2)))
                    print("Here is your {}, Enjoy!".format(coffee))
        except:
            print("Fix your input please")



def main():
    coffee_machine()











if __name__ == '__main__':
    main()


