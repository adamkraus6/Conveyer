from kraus_adam.Belt import Belt
from kraus_adam.Station import Station

class Conveyer:
    def __init__(self):
        """
        Conveyer constructor
        """
        self.__sections = [Belt(), Belt(), Station(), Belt(), Belt(), Station()]
    
    def addSection(self, section):
        """
        Adds a new section to the end of the conveyer
        :param section: New section
        :type section: Station or Belt
        """
        self.__sections.append(section)
    
    def addBox(self, box):
        """
        Adds a box to first section if available
        :param box: New box
        :type box: Box
        """
        if(len(self.__sections) > 0):
            self.__sections[0].addBox(box)

    # GRADING: ITER_ALL
    def __iter__(self):
        """
        Setup for iterator
        :return: Self for iteration
        :rtype: Box
        """
        self.__index = -1
        return self

    def __next__(self):
        """
        Gets next item in iteration
        :return: Next section
        :rtype: Station or Belt
        """
        self.__index += 1
        if(self.__index < len(self.__sections)):
            return self.__sections[self.__index]
        raise StopIteration
    
    def stations(self):
        """
        Yields all stations in conveyer
        :return: All stations
        :rtype: Station[]
        """
        for section in self:
            if(type(section) == Station):
                yield section
    
    def clear(self):
        """
        Clears current conveyer sections
        """
        self.__sections = []

    def __str__(self):
        """
        Appends all section info horizontally
        :return: Conveyer sections
        :rtype: String
        """
        str1, str2, str3 = "", "", ""
        for section in self.__sections:
            str1 += str(section)[0:4]
            str2 += str(section)[5:9]
            str3 += str(section)[10:14]
        return str1 + "\n" + str2 + "\n" + str3