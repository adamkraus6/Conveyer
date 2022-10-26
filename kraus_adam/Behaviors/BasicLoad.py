# GRADING: BASIC_LOAD
class BasicLoad:
    def __init__(self, units):
        self.__units = units
    
    def load(self, station):
        station.getBox().addUnits(self.__units)