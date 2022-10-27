class Belt:
    def __init__(self):
        """
        Belt constructor
        """
        self.__box = None

    def moveBox(self, box):
        """
        Move a new box into belt, return old box
        :param box: New box
        :type box: Box
        :return: Old box
        :rtype: Box
        """
        oldBox = self.__box
        self.__box = box
        return oldBox

    def addBox(self, box):
        """
        Place a box on belt if not occupied
        :param box: New box
        :type box: Box
        """
        if(self.__box == None):
            self.__box = box
    
    def __str__(self):
        """
        Prints box info if applicable and ---- to specify a belt
        :return: Belt info
        :rtype: String
        """
        if(self.__box == None):
            return "    \n    \n----"
        else:
            return str(self.__box) + "\n----"