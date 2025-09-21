import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine_on = True
    while machine_on:
        choice = input("small/ medium/ large/ off/ report: ").lower()

        if choice == "off":
            print("Machine turned off")
            machine_on = False
        elif choice == "report":
            print(f"Bread: {data.resources['bread']} slice(s)")
            print(f"Ham: {data.resources['bread']} slice(s)")
            print(f"Cheese: {data.resources['cheese']} ounce(s)")
        elif choice in recipes:
            sandwhich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwhich["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, sandwhich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwhich["ingredients"])
        else:
            print("Not a valid option")


if __name__=="__main__":
    main()
