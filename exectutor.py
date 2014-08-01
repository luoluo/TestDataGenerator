from myConfig import MyConfig
from generator import *
class Exectutor():
    def __init__(self):
        pass
    def run(self):
        testDataGenerator = TestDataGenerator()
        testDataGenerator.loadDescriptionFromFIle("generate.cfg")
        testDataGenerator.generate()
