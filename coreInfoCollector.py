from myConfig import MyConfig
class CoreInfoCollector:
    def __init__(self, inputFile):
        self.infoDescriptions = []
        self.inputFile = inputFile

    def collect(self):
        for infoDescription in self.infoDescriptions:
            self.collectOne(infoDescription)

    def collectOne(self, infoDescription):
        allInfos = open(self.inputFile)
        dict = {}
        field = infoDescription.getField()
        type = infoDescription.getType()
        for info in allInfos:
            infoList = info.strip().split("\t")
            infoToCollect = infoList[field]
            if type == 3:
               infoToCollect = infoToCollect.split()[1]
            elif type == 4:
               infoToCollect = infoToCollect.split()[0]
            else:
                pass
            if infoToCollect in dict:
                dict[infoToCollect] += 1
            else:
                dict[infoToCollect] = 1
        print dict
        return dict

    def collectTime(self, infoDescription):
        pass

    def collectDate(self, infoDescription):
        pass

    def loadDescription(self):
        self.infoDescriptions.append(InfoDescription(0, 0))
        self.infoDescriptions.append(InfoDescription(1, 1))

    def loadDescriptionFromFIle(self, fileName):
        myConfig = MyConfig(fileName)
        descriptions = myConfig.getListOfList("description1", "description")
        for description in descriptions:
            self.infoDescriptions.append(InfoDescription(description[0], description[1]))

class InfoDescription:
    def __init__(self, field, type):
        self.type = type
        self.field = field
        self.split = ''

    def getType(self):
        return self.type

    def getField(self):
        return self.field

    def getSplit(self):
        return self.split

if __name__ == "__main__":
    coreInfoCollector = CoreInfoCollector("coreInfoInput")
 #   coreInfoCollector.loadDescription()
    coreInfoCollector.loadDescriptionFromFIle("coreInfo.cfg")
    coreInfoCollector.collect()
