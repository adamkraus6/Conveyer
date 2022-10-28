from kraus_adam.Box import Box

class Station:
    """
    Station portion of conveyor
    """
    def __init__(self, loadBeh=None, packBeh=None):
        """
        Station constructor
        :param loadBeh: Loading behavior
        :type loadBeh: BasicLoad or PercentLoad
        :param packBeh: Packaging behavior
        :type packBeh: BasicPack or RestrictedPack
        """
        self.__loadBeh = loadBeh 
        self.__packBeh = packBeh
        self.__box = None
    
    def moveBox(self, box):
        """
        Move a new box into belt, return old box. Does loading and packaging if applicable
        :param box: New box
        :type box: Box
        :return: Old box
        :rtype: Box
        """
        self.pack()
        oldBox = self.__box
        self.__box = box
        if(self.__box != None):
            self.load()
        return oldBox

    def takeBox(self):
        """
        Removes box
        :return: Old box
        :rtype: Box
        """
        box = self.__box
        self.__box = None
        return box

    def load(self):
        """
        Does loading behavior if applicable
        """
        if(self.__loadBeh != None):
            self.__loadBeh.load(self)
    
    def pack(self):
        """
        Does packaging behavior if applcable
        """
        if(self.__packBeh != None):
            self.__packBeh.pack(self)

    def getPackInfo(self):
        """
        Gets packaging info if applicable
        :return: Packaging info
        :rtype: String
        """
        if(self.__packBeh == None):
            return "Packaging: None"
        else:
            return self.__packBeh.packInfo();

    def addBox(self, box):
        """
        Place a box on belt if not occupied
        :param box: New box
        :type box: Box
        """
        if(self.__box == None):
            self.__box = box
    
    def getBox(self):
        """
        Gets current box
        :return: Current box
        :rtype: Box
        """
        return self.__box
    
    def hasBox(self):
        """
        Checks if currently has a box
        :return: True if occupied
        :rtype: Boolean
        """
        if(self.__box == None):
            return False
        return True

    def __str__(self):
        """
        Prints box info if applicable and XXXX to specify a station
        :return: Belt info
        :rtype: String
        """
        if(self.__box == None):
            return "    \n    \nXXXX"
        else:
            return str(self.__box) + "\nXXXX"