class Player:
    def __init__(self, name=None):
        self.__name = name if name != "" or name is not None else "Guest"
        self.__properties = { "Statitics": [] }
        pass

    def get(self, prop: str):
        return self.__properties.get(prop, None)

    def set(self, prop: str, value):
        self.__properties[prop] = value
        return self

    def with_property(self, prop: str, value=None):
        self.__properties[prop] = value
        return self
