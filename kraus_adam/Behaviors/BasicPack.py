class BasicPack:
    def __init__(self, fullBoxes):
        self.fullBoxes = fullBoxes;
        self.boxes = []
        self.packaged = 0
    
    def packInfo(self):
        info = "Packages every " + str(self.fullBoxes) + " boxes\n" + \
            "Currently has unpackaged box ids: " + str([box.getID() for box in self.boxes])[1:-1] + \
            "\nPackages Complete: " + str(self.packaged)
        return info
    
    def pack(self, station):
        stationBox = station.getBox()
        if(stationBox != None):
            if(stationBox.isFull()):
                station.takeBox()
                self.boxes.append(stationBox)
                if(len(self.boxes) == self.fullBoxes):
                    self.boxes.clear()
                    self.packaged += 1