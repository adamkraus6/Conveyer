class Box:
    BOX_ID = 1

    def __init__(self, max=10):
        self.__id = Box.BOX_ID
        Box.BOX_ID += 1
        self.__units = 0
        self.__maxUnits = max
    
    def addUnits(self, units):
        self.__units = min(self.__maxUnits, self.__units + units)
    
    def getID(self):
        return self.__id

    def getUnits(self):
        return self.__units

    def getMaxUnits(self):
        return self.__maxUnits

    def isFull(self):
        return self.__units == self.__maxUnits;
    
    def __str__(self):
        return str(self.__id).ljust(4) + "\n" + str(self.__units).ljust(4)
