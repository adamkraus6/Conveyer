# GRADING: RESTRICTED_PACKAGE
class RestrictedPack:
    def __init__(self, waitBoxes, minUnits, maxUnits):
        self.__waitBoxes = waitBoxes
        self.__minUnits = minUnits
        self.__maxUnits = maxUnits
        self.__sizeRange = range(minUnits, maxUnits+1)
        self.__boxes = []
        self.__packaged = 0

    def packInfo(self):
        info = "Size range [" + str(self.__minUnits) + ", " + str(self.__maxUnits) + \
            "]\nPackages every " + str(self.__waitBoxes) + " boxes\n" + \
            "Currently has unpackaged box ids: " + str([box.getID() for box in self.__boxes])[1:-1] + \
            "\nPackages Complete: " + str(self.__packaged)
        return info
    
    def pack(self, station):
        stationBox = station.getBox()
        if(stationBox != None):
            if(stationBox.getUnits() in self.__sizeRange):
                station.takeBox()
                self.__boxes.append(stationBox)
                if(len(self.__boxes) == self.__waitBoxes):
                    self.__boxes.clear()
                    self.__packaged += 1