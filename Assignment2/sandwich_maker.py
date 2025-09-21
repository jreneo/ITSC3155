
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for item, amount in ingredients.items():
            if amount > self.machine_resources.get(item, 0):
                print("Not enough ingredients: ",item)
                return False
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"Here is your {sandwich_size} sandwhich. Enjoy!")