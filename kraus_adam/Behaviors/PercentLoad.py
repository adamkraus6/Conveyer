class PercentLoad:
    def __init__(self, percent):
        self.percent = percent
    
    def load(self, station):
        maxUnits = station.getBox().getMaxUnits()
        units = (maxUnits * self.percent) / 100
        station.getBox().addUnits(int(units))