class Box:
    BOX_ID = 1

    def __init__(self, max=10):
        self.id = Box.BOX_ID
        Box.BOX_ID = Box.BOX_ID + 1
        self.units = 0
        self.maxUnits = max
    
    def __str__(self):
        return str(self.id).ljust(4) + "\n" + str(self.units).ljust(4)
