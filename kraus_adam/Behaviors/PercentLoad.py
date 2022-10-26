# GRADING: PERCENT_LOAD
class PercentLoad:
    def __init__(self, percent):
        self.__percent = percent
    
    def load(self, station):
        maxUnits = station.getBox().getMaxUnits()
        units = (maxUnits * self.__percent) / 100
        station.getBox().addUnits(int(units))