import ConfigParser
import io
import ast
class MyConfig:
    def __init__(self, configureFile):
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(configureFile)

    def getInt(self, section1, section2):
        return int(self.config.get(section1, section2))

    def getString(self, section1, section2):
        return self.config.get(section1, section2)

    def getList(self, section1, section2):
        #read list configure as a list
        liststr = self.config.get(section1, section2)
        list = liststr.lstrip("[").rstrip("]").replace(",", "").split()
        return list

    def getIntList(self, section1, section2):
        charList = self.getList(section1, section2)
        list = map(int, charList)
        return list

    def getListOfList(self, section1, section2):
        lists = []
        liststr = self.getString(section1, section2)
        liststrs = liststr.lstrip("[").rstrip("]").split(";")
        for liststr in liststrs:
            list = liststr.strip().lstrip("[").rstrip("]").replace(",", "").split()
            list = map(int, list)
            lists.append(list)
        return lists

    def getDict(self, section1, section2):
        #covert string to map
        dictstr = self.config.get(section1, section2)
        dict = ast.literal_eval(dictstr)
        return dict

if __name__ == "__main__":
    myConfig = MyConfig("example.cfg")
    print myConfig.getString("mysql", "user")
    print myConfig.getList("mysql", "list")
    print myConfig.getIntList("mysql", "list")
    print myConfig.getDict("mysql", "dict")
    print myConfig.getListOfList("mysql", "listOfList")

