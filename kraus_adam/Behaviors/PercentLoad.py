# GRADING: PERCENT_LOAD
class PercentLoad:
    """
    Percentage loading behavior
    """
    def __init__(self, percent):
        """
        Percent Loading constructor
        :param units: Percent of box to load
        :type units: Integer
        """
        self.__percent = percent
    
    def load(self, station):
        """
        Loading behavior function
        :param station: Station with box to load
        :type station: Station
        """
        maxUnits = station.getBox().getMaxUnits()
        units = (maxUnits * self.__percent) / 100
        station.getBox().addUnits(int(units))