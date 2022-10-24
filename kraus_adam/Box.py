class Box:
    BOX_ID = 1

    def __init__(self, max=10):
        self.id = Box.BOX_ID # TODO: private
        Box.BOX_ID += 1
        self.units = 0 # TODO: private
        self.maxUnits = max # TODO: private
    
    def addUnits(self, units):
        self.units = min(self.maxUnits, self.units + units)
    
    def getID(self):
        return self.id

    def getMaxUnits(self):
        return self.maxUnits
    
    def __str__(self):
        return str(self.id).ljust(4) + "\n" + str(self.units).ljust(4)
