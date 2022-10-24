class RestrictedPack:
    def __init__(self, fullBoxes, minUnits, maxUnits):
        self.fullBoxes = fullBoxes
        self.minUnits = minUnits
        self.maxUnits = maxUnits
        self.sizeRange = range(minUnits, maxUnits+1)
        self.boxes = []
        self.packaged = 0

    def packInfo(self):
        info = "Size range [" + str(self.minUnits) + ", " + str(self.maxUnits) + \
            "]\nPackages every " + str(self.fullBoxes) + " boxes\n" + \
            "Currently has unpackaged box ids: " + str([box.getID() for box in self.boxes])[1:-1] + \
            "\nPackages Complete: " + str(self.packaged)
        return info
    
    def pack(self, station):
        stationBox = station.getBox()
        if(stationBox != None):
            if(stationBox.getUnits() in self.sizeRange):
                station.takeBox()
                self.boxes.append(stationBox)
                if(len(self.boxes) == self.fullBoxes):
                    self.boxes.clear()
                    self.packaged += 1