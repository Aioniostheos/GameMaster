class Player:
    def __init__(self, name=None, properties={ "Statitics": [] }):
        self.__name = name if name != "" or name is not None else "Guest"
        self.__properties = properties
        pass

    def getName(self):
        return self.__name

    def get(self, prop: str):
        return self.__properties.get(prop, None)

    def getProperties(self):
        return self.__properties

    def set(self, prop: str, value):
        self.__properties[prop] = value
        return self

    def with_property(self, prop: str, value=None):
        self.__properties[prop] = value
        return self.__properties
