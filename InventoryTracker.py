# Final Exam AIDI 2004 - Joel

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity

    def updateStock(self, item_name, new_quantity):
        """
        Updates the quantity of an existing item in inventory.
        """
        if item_name in self.inventory:
            self.inventory[item_name] = new_quantity
        else:
            print("Item not found")
