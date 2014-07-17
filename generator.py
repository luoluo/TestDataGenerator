import random
from myConfig import MyConfig
class BaseTestDataGenerator:
    def __init__(self):
        self.Source = []
    def generateOneItem(self, length):
        entity = []
        while len(entity) < length:
            entity.append(self.chooseOne()) 
        return ''.join(entity)

    def chooseOne(self):
        curSource = self.Source
        return curSource[random.randint(0, len(curSource)-1)]

class NumberGeneretor(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.Source = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class StringGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.Source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class MixGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.Source = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class IPGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
    def generateOneItem(self, length = 4):
        entity = []
        count = 0
        while count < length:
            entity.append(self.chooseOne())
            entity.append(".")
            count += 1
        return ''.join(entity).rstrip(".")
    def chooseOne(self):
        return str(random.randint(0, 255))

class EmailGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.mixGenerator = MixGenerator()
    def generateOneItem(self, length):
        email = self.mixGenerator.generateOneItem(6)
        email += ("@")
        email += (self.mixGenerator.generateOneItem(2))
        email += (".com")
        return email

class TimeGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.mixGenerator = MixGenerator()
        self.dateGenerator = DateGenerator()
    def generateOneItem(self, length = 0):
        time = ""
        time += self.chooseOne(23)
        time += ":"
        time += self.chooseOne(59)
        time += ":"
        time += self.chooseOne(59)
        time = self.dateGenerator.generateOneItem() + " " + time
        return time
    def chooseOne(self, max):
        timePart = str(random.randint(0, max))
        if len(timePart) == 1:
            timePart = '0' + timePart
        return timePart

class DateGenerator(BaseTestDataGenerator):
    def __init__(self):
        BaseTestDataGenerator.__init__(self)
        self.mixGenerator = MixGenerator()
    def generateOneItem(self, length = 0):
        date = ""
        date += self.chooseOne(2014, 2014)
        date += "-"
        date += self.chooseOne(1, 12)
        date += "-"
        date += self.chooseOne(1, 28)
        return date
    def chooseOne(self, min, max):
        datePart = str(random.randint(min, max))
        if len(datePart) == 1:
            datePart = '0' + datePart
        return datePart

class TestDataGenerator:
    def __init__(self):
        self.numberGenerator = NumberGeneretor()
        self.charGenerator = StringGenerator()
        self.mixGenerator = MixGenerator()
        self.timeGenerator= TimeGenerator()
        self.iPGenerator = IPGenerator()
        self.emailGenerator = EmailGenerator()
        self.dataDescriptions = []
        self.amount = 0
        #self.loadDescription()
        #self.loadDescriptionFromFIle("generate.cfg")
        self.splitChar = '\t'

    def loadDescription(self):
        self.dataDescriptions.append(DataDescription(0, 5))
        self.dataDescriptions.append(DataDescription(1, 6))
        self.dataDescriptions.append(DataDescription(1, 19))

    def loadDescriptionFromFIle(self, fileName):
        myConfig = MyConfig(fileName)
        descriptions = myConfig.getListOfList("description1", "description")
        self.amount = myConfig.getInt("description1", "amount")
        for description in descriptions:
            self.dataDescriptions.append(DataDescription(description[0], description[1]))

    def generateOne(self):
        entity = []
        for dataDescription in self.dataDescriptions:
            entity.append(self.generateOneBit(dataDescription))
            entity.append('\t')
        return ''.join(entity)

    def generateOneBit(self, dataDescription):
        type = dataDescription.getType()
        length = dataDescription.getLength()
        generator = self.getGenerator(type)
        return generator.generateOneItem(length)

        self.mixGenerator = MixGenerator()
        self.mixGenerator = TimeGenerator()
        self.iPGenerator = IPGenerator()
        self.emailGenerator = EmailGenerator()
    def getGenerator(self, type):
        if type == 0:
            return self.numberGenerator
        elif type == 1:
            return self.charGenerator
        elif type == 2:
            return self.mixGenerator
        elif type == 3:
            return self.timeGenerator
        elif type == 4:
            return self.iPGenerator
        elif type == 5:
            return self.emailGenerator

    def generate(self):
        count = 0
        while count < self.amount:
            print self.generateOne()
            count += 1

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
    #testNumberGenerator = NumberGeneretor()
    #print testNumberGenerator.generateOneItem(12)
    #testNumberGenerator = StringGenerator()
    #print testNumberGenerator.generateOneItem(12)
    #testNumberGenerator = MixGenerator()
    #print testNumberGenerator.generateOneItem(12)
    #testNumberGenerator = IPGenerator()
    #print testNumberGenerator.generateOneItem()
    #testNumberGenerator = EmailGenerator()
    #print testNumberGenerator.generateOneItem()
    #testNumberGenerator = TimeGenerator()
    #print testNumberGenerator.generateOneItem()
    #testNumberGenerator = DateGenerator()
    #print testNumberGenerator.generateOneItem()

    testDataGenerator = TestDataGenerator()
    testDataGenerator.loadDescriptionFromFIle("generate.cfg")
    testDataGenerator.generate()
