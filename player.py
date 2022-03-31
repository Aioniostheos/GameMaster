class Player:
    def __init__(self, name):
        self.__name = name
        self.__properties = {}
        pass

    def get(self, prop: str):
        return self.__properties.get(prop, None)

    def set(self, prop: str, value):
        self.__properties[prop] = value
        return self

    def with_property(self, prop: str, value=None):
        self.__properties[prop] = value
        return self
