class Station:
    def __init__(self, loadBeh=None, packBeh=None):
        self.loadBeh = loadBeh # TODO: private
        self.packBeh = packBeh # TODO: private
        self.Box = None # TODO: private
    
    def moveBox(self, box):
        oldBox = self.Box
        self.Box = box
        if(self.loadBeh != None and box != None):
            self.loadBeh.load(self)
        return oldBox

    def load(self):
        self.loadBeh.load(self)
    
    def pack(self):
        self.packBeh.pack()

    def getPackInfo(self):
        if(self.packBeh == None):
            return "Packaging: None"
        else:
            return self.loadBeh.loadInfo();

    def addBox(self, box):
        if(self.Box == None):
            self.Box = box
    
    def getBox(self):
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