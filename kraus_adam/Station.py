class Station:
    def __init__(self):
        self.loadBeh = None
        self.packBeh = None
        self.Box = None
    
    def moveBox(self, box):
        oldBox = self.Box
        self.Box = box
        if(self.loadBeh != None):
            self.loadBeh()
        return oldBox

    def setLoad(self, load):
        self.loadBeh = load;
    
    def setPack(self, pack):
        self.packBeh = pack;

    def addBox(self, box):
        if(self.Box == None):
            self.Box = box

    def __str__(self):
        if(self.Box == None):
            return "    \n    \nXXXX"
        else:
            return str(self.Box) + "\nXXXX"