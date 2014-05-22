from myConfig import MyConfig
from generator import DataDescription
class PreDeal:
    def __init__(self, inputFile):
        self.dataDescriptions = []
        self.inputFile = inputFile

    def check(self):
        allLines = open(self.inputFile)
        for line in allLines:
            self.checkOneLine(line.strip())

    def checkOneLine(self, line):
        lists = line.split("\t")
        if len(lists) == len(self.dataDescriptions):
            print line

    def loadDescription(self):
        self.dataDescriptions.append(DataDescription(0, 3))
        self.dataDescriptions.append(DataDescription(0, 3))

    def loadDescriptionFromFIle(self, fileName):
        myConfig = MyConfig(fileName)
        descriptions = myConfig.getListOfList("description1", "description")
        self.amount = myConfig.getInt("description1", "amount")
        for description in descriptions:
            self.dataDescriptions.append(DataDescription(description[0], description[1]))

if __name__ == "__main__":
    preDeal = PreDeal("predealInput")
#    preDeal.loadDescription()
    preDeal.loadDescriptionFromFIle("generate.cfg")
    preDeal.check()
