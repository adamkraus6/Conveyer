class Belt:
    def __init__(self):
        self.__box = None

    def moveBox(self, box):
        oldBox = self.__box
        self.__box = box
        return oldBox

    def addBox(self, box):
        if(self.__box == None):
            self.__box = box
    
    def __str__(self):
        if(self.__box == None):
            return "    \n    \n----"
        else:
            return str(self.__box) + "\n----"