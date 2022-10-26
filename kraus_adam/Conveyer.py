from kraus_adam.Belt import Belt
from kraus_adam.Station import Station

class Conveyer:
    def __init__(self):
        self.__sections = [Belt(), Belt(), Station(), Belt(), Belt(), Station()] # TODO: private
    
    def addSection(self, section):
        self.__sections.append(section)
    
    def addBox(self, box):
        if(len(self.__sections) > 0):
            self.__sections[0].addBox(box)

    # GRADING: ITER_ALL
    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if(self.index < len(self.__sections)):
            return self.__sections[self.index]
        raise StopIteration
    
    def stations(self):
        for section in self:
            if(type(section) == Station):
                yield section
    
    def clear(self):
        self.__sections = []

    def __str__(self):
        str1, str2, str3 = "", "", ""
        for section in self.__sections:
            str1 += str(section)[0:4]
            str2 += str(section)[5:9]
            str3 += str(section)[10:14]
        return str1 + "\n" + str2 + "\n" + str3