from kraus_adam.Belt import Belt
from kraus_adam.Station import Station

class Conveyor:
    """
    Station/Belt collection class
    """
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
        :rtype: Conveyor
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
    
    def getStationIter(self):
        return self.StationIter(self.__sections)

    class StationIter:
        """
        Iterations over just the stations in the conveyor
        """
        def __init__(self, sections):
            """
            Station iterator constructor
            :param sections: Sections of the conveyor
            :type sections: Section[]
            """
            self.__sections = sections
        
        # GRADING: ITER_STATION
        def __iter__(self):
            """
            Setup for station iterator
            :return: Self for iteration
            :rtype: StationIter
            """
            self.__index = -1
            return self

        def __next__(self):
            """
            Gets next station in iteration
            :return: Next Station
            :rtype: Station
            """
            self.__index += 1
            try:
                while(type(self.__sections[self.__index]) == Belt):
                    self.__index += 1
                return self.__sections[self.__index]
            except:
                raise StopIteration
    
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