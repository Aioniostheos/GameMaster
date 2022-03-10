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
