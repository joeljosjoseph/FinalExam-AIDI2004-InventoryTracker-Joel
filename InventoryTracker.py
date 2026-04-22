# Final Exam AIDI 2004 - Joel

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
