class Inventory:
    def __init__(self):
        self.items = {}

    def add_coffee(self, coffee):
        self.items[coffee.get_name()] = coffee

    def get_inventory(self):
        return self.items
