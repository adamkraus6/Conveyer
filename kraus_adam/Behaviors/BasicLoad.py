class BasicLoad:
    def __init__(self, units):
        self.units = units
    
    def load(self, station):
        station.getBox().addUnits(self.units)