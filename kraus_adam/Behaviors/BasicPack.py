# GRADING: BASIC_PACKAGE
class BasicPack:
    def __init__(self, fullBoxes):
        self.__fullBoxes = fullBoxes;
        self.__boxes = []
        self.__packaged = 0
    
    def packInfo(self):
        info = "Packages every " + str(self.__fullBoxes) + " boxes\n" + \
            "Currently has unpackaged box ids: " + str([box.getID() for box in self.__boxes])[1:-1] + \
            "\nPackages Complete: " + str(self.__packaged)
        return info
    
    def pack(self, station):
        stationBox = station.getBox()
        if(stationBox != None):
            if(stationBox.isFull()):
                station.takeBox()
                self.__boxes.append(stationBox)
                if(len(self.__boxes) == self.__fullBoxes):
                    self.__boxes.clear()
                    self.__packaged += 1