from pickletools import string1
from Belt import Belt
from Station import Station

class Conveyer:
    def __init__(self):
        self.sections = [Belt(), Belt(), Station(), Belt(), Belt(), Station()]
    
    def addSection(self, section):
        self.sections.append(section)
    
    def addBox(self, box):
        if(len(self.sections) > 0):
            self.sections[0].addBox(box)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if(self.index < len(self.sections)):
            return self.sections[self.index]
        raise StopIteration

    def __str__(self):
        str1, str2, str3 = "", "", ""
        for section in self.sections:
            str1 += str(section)[0:4]
            str2 += str(section)[5:9]
            str3 += str(section)[10:14]
        return str1 + "\n" + str2 + "\n" + str3