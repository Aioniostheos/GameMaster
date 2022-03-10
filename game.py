class Game:
    def __init__(self, players, gametype=None, gamevariant=None):
        self.__players = players
        self.__gametype = gametype
        self.__gamevariant = gamevariant

        self.__status = "En Cours"

        self.__creation_date = time.asctime()[4:]
        self.__end_date = None

        self.save()

    def save(self):
        pass
