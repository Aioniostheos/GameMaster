from datetime import time


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
        pass
        #TODO

    def load(self):
        pass
        #TODO

    def get_creation_date(self):
        return self.__creation_date

    def get_players(self):
        return self.__players

    def pause(self):
        self.__status = "En pause"
        self.save()
