# GRADING: BASIC_LOAD
class BasicLoad:
    def __init__(self, units):
        """
        Basic Loading constructor
        :param units: Number of units to load
        :type units: Integer
        """
        self.__units = units
    
    def load(self, station):
        """
        Loading behavior function
        :param station: Station with box to load
        :type station: Station
        """
        station.getBox().addUnits(self.__units)