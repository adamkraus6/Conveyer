from Box import Box

class Station:
    def __init__(self, loadBeh=None, packBeh=None):
        self.loadBeh = loadBeh # TODO: private
        self.packBeh = packBeh # TODO: private
        self.Box = None # TODO: private
    
    def moveBox(self, box):
        self.pack()
        oldBox = self.Box
        self.Box = box
        if(self.Box != None):
            self.load()
        return oldBox

    def takeBox(self):
        box = self.Box
        self.Box = None
        return box

    def load(self):
        if(self.loadBeh != None):
            self.loadBeh.load(self)
    
    def pack(self):
        if(self.packBeh != None):
            self.packBeh.pack(self)

    def getPackInfo(self):
        if(self.packBeh == None):
            return "Packaging: None"
        else:
            return self.packBeh.packInfo();

    def addBox(self, box):
        if(self.Box == None):
            self.Box = box
    
    def getBox(self) -> Box:
        return self.Box
    
    def hasBox(self):
        if(self.Box == None):
            return False
        return True

    def __str__(self):
        if(self.Box == None):
            return "    \n    \nXXXX"
        else:
            return str(self.Box) + "\nXXXX"