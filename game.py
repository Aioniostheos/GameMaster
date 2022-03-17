import time


class Game:
    def __init__(self, players, game_type=None, game_variant=None,
                 status="En Cours", creation_date=time.asctime()[4:], end_date=None):
        self.__players = players
        self.__game_type = game_type
        self.__game_variant = game_variant

        self.__status = status

        self.__creation_date = creation_date
        self.__end_date = end_date

    def save(self):
        main.GAMES[self.get_creation_date()] = self

    def pause(self):
        self.__status = "En pause"
        self.save()

    def end(self):
        self.__status = "Finie"
        self.__end_date = time.asctime()[4:]
        self.save()

    def get_game_type(self):
        if self.__game_type is None and self.__game_variant is None:
            return ""
        elif self.__game_variant is None:
            return self.__game_type
        else:
            return self.__game_type + "-" + self.__game_variant

    def get_creation_date(self):
        return self.__creation_date

    def get_players(self):
        return self.__players

    def get_status(self):
        return self.__status
