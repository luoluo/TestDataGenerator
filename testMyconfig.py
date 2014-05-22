from myConfig import MyConfig
if __name__ == "__main__":
    myConfig = MyConfig("example.cfg")
    print myConfig.getString("mysql", "user")
    print myConfig.getList("mysql", "list")
    print myConfig.getIntList("mysql", "list")
    print myConfig.getDict("mysql", "dict")
