# GRADING: BASIC_PACKAGE
class BasicPack:
    """
    Basic packaging behavior
    """
    def __init__(self, waitBoxes):
        """
        Basic Packaging constructor
        :param waitBoxes: Number of full boxes to keep before packaging
        :type waitBoxes: Integer
        """
        self.__waitBoxes = waitBoxes;
        self.__boxes = []
        self.__packaged = 0
    
    def packInfo(self):
        """
        Get packaging information
        :return: Packaging info
        :rtype: String
        """
        info = "Packages every " + str(self.__waitBoxes) + " boxes\n" + \
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
            if(stationBox.isFull()):
                station.takeBox()
                self.__boxes.append(stationBox)
                if(len(self.__boxes) == self.__waitBoxes):
                    self.__boxes.clear()
                    self.__packaged += 1