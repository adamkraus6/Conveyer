class Belt:
    def __init__(self):
        self.Box = None # TODO: private

    def moveBox(self, box):
        oldBox = self.Box
        self.Box = box
        return oldBox

    def addBox(self, box):
        if(self.Box == None):
            self.Box = box
    
    def __str__(self):
        if(self.Box == None):
            return "    \n    \n----"
        else:
            return str(self.Box) + "\n----"