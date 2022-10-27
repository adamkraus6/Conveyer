# GRADING: RESTRICTED_PACKAGE
class RestrictedPack:
    def __init__(self, waitBoxes, minUnits, maxUnits):
        """
        Basic Packaging constructor
        :param waitBoxes: Number of full boxes to keep before packaging
        :type waitBoxes: Integer
        :param minUnits: Minimum units in box for packaging
        :type minUnits: Integer
        :param maxUnits: Maximum units in box for packaging
        :type minUnits: Integer
        """
        self.__waitBoxes = waitBoxes
        self.__minUnits = minUnits
        self.__maxUnits = maxUnits
        self.__sizeRange = range(minUnits, maxUnits+1)
        self.__boxes = []
        self.__packaged = 0

    def packInfo(self):
        """
        Get packaging information
        :return: Packaging info
        :rtype: String
        """
        info = "Size range [" + str(self.__minUnits) + ", " + str(self.__maxUnits) + \
            "]\nPackages every " + str(self.__waitBoxes) + " boxes\n" + \
            "Currently has unpackaged box ids: " + str([box.getID() for box in self.__boxes])[1:-1] + \
            "\nPackages Complete: " + str(self.__packaged)
        return info
    
    def pack(self, station):
        """
        Packaging behavior function
        :param station: Station with full box to package
        :type station: Station
        """
        stationBox = station.getBox()
        if(stationBox != None):
            if(stationBox.getUnits() in self.__sizeRange):
                station.takeBox()
                self.__boxes.append(stationBox)
                if(len(self.__boxes) == self.__waitBoxes):
                    self.__boxes.clear()
                    self.__packaged += 1