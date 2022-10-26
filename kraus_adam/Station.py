from kraus_adam.Box import Box

class Station:
    def __init__(self, loadBeh=None, packBeh=None):
        self.__loadBeh = loadBeh 
        self.__packBeh = packBeh
        self.__box = None
    
    def moveBox(self, box):
        self.pack()
        oldBox = self.__box
        self.__box = box
        if(self.__box != None):
            self.load()
        return oldBox

    def takeBox(self):
        box = self.__box
        self.__box = None
        return box

    def load(self):
        if(self.__loadBeh != None):
            self.__loadBeh.load(self)
    
    def pack(self):
        if(self.__packBeh != None):
            self.__packBeh.pack(self)

    def getPackInfo(self):
        if(self.__packBeh == None):
            return "Packaging: None"
        else:
            return self.__packBeh.packInfo();

    def addBox(self, box):
        if(self.__box == None):
            self.__box = box
    
    def getBox(self) -> Box:
        return self.__box
    
    def hasBox(self):
        if(self.__box == None):
            return False
        return True

    def __str__(self):
        if(self.__box == None):
            return "    \n    \nXXXX"
        else:
            return str(self.__box) + "\nXXXX"