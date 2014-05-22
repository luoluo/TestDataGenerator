import random
class BaseTestDataGenerator:
    def __init__(self, type):
        self.type = type
        self.Source = []
        self.Source.append(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.Source.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    def generateOneItem(self, length):
        entity = []
        while len(entity) < length:
            entity.append(self.chooseOne()) 
        return ''.join(entity)

    def chooseOne(self):
        curSource = self.Source[self.type]
        return curSource[random.randint(0, len(curSource)-1)]


class TestDataGenerator:
    def __init__(self):
        self.numberGenerator = BaseTestDataGenerator(0)
        self.charGenerator = BaseTestDataGenerator(1)
        self.dataDescriptions = []
        self.loadDescription()
        self.splitChar = '\t'

    def loadDescription(self):
        self.dataDescriptions.append(DataDescription(0, 5))
        self.dataDescriptions.append(DataDescription(1, 6))
        self.dataDescriptions.append(DataDescription(1, 19))

    def loadDescriptionFromFIle(self):
        #TODO
        return

    def generateOne(self):
        entity = []
        for dataDescription in self.dataDescriptions:
            entity.append(self.generateOneBit(dataDescription))
            entity.append('\t')
        return ''.join(entity)

    def generateOneBit(self, dataDescription):
        type = dataDescription.getType()
        length = dataDescription.getLength()
        generator = self.getBaseGenerator(type)
        return generator.generateOneItem(length)

    def getBaseGenerator(self, type):
        if type == 0:
            return self.numberGenerator
        else:
            return self.charGenerator

class DataDescription:
    def __init__(self, type, length):
        self.type = type
        self.length = length
        self.split = ''

    def getType(self):
        return self.type

    def getLength(self):
        return self.length

    def getSplit(self):
        return self.split

if __name__ == "__main__":
    testDataGenerator = TestDataGenerator()
    print testDataGenerator.generateOne()
