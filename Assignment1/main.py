### Data ###
from math import trunc
from random import choice

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if amount > self.machine_resources[item]:
                print("Insufficient resources for sandwhich: ", item)
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins for payment")
        dollars = int(input("how many dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05

        total = round(dollars + half_dollars + quarters + nickels, 2)
        print("Total payment: ", total)
        return total

    def transaction_result(self, total, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost > total:
            print("Insufficient payment for sandwhich")
            return False
        else:
            change = round(total - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return  True
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print("Make sandwhich")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
machine_on = True
while machine_on:
    print("What would you like to do?")
    choice = input("small/ medium/ large/ off/ report: ").lower()


    if choice == "off":
        print("Machine turned off")
        machine_on = False
    elif choice == "report":
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} ounce(s)")
    elif choice in recipes:
        sandwhich = recipes[choice]
        if machine.check_resources(sandwhich["ingredients"]):
            coins = machine.process_coins()
            if machine.transaction_result(coins, sandwhich["cost"]):
                machine.make_sandwich(choice, sandwhich["ingredients"])
    else: print("Not a valid option")
