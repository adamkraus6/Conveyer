class Box:
    """
    Box that holds units
    """
    BOX_ID = 1

    def __init__(self, max=10):
        """
        Box constructor
        :param max: Max units that can fit in box, default 10
        :type max: Integer
        """
        self.__id = Box.BOX_ID
        Box.BOX_ID += 1
        self.__units = 0
        self.__maxUnits = max
    
    def addUnits(self, units):
        """
        Adds units to a box, will not overfill
        :param units: Number of units to add
        :type units: Integer
        """
        self.__units = min(self.__maxUnits, self.__units + units)
    
    def getID(self):
        """
        Gets box id
        :return: Box id
        :rtype: Integer
        """
        return self.__id

    def getUnits(self):
        """
        Gets current units in box
        :return: Current units
        :rtype: Integer
        """
        return self.__units

    def getMaxUnits(self):
        """
        Gets max units that can fit in box
        :return: Max units for box
        :rtype: Integer
        """
        return self.__maxUnits

    def isFull(self):
        """
        Checks if box is full
        :return: True if full
        :rtype: Boolean
        """
        return self.__units == self.__maxUnits;
    
    def __str__(self):
        """
        Prints box id and current units
        :return: Box info
        :rtype: String
        """
        return str(self.__id).ljust(4) + "\n" + str(self.__units).ljust(4)
