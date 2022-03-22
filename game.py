import logging
import time
from pathlib import Path
from xml.etree import ElementTree

import main

logger = logging.getLogger("PyLog")


def load(game_creation_date):
    main.GAMES.get(game_creation_date)
    pass


def loadall():
    games = {}
    paths = list(Path('./data/games/').glob('**/*.xml'))
    logger.info("Found %s saves", len(paths))
    for path in paths:
        logger.info("Loading %s...", path)
        with path.open() as file:
            root = ElementTree.parse(file).getroot()
            if root.tag != "game":
                logger.warning("%s is not a save ! Skipping file...", path)
                continue

    logger.info("Loaded %s saves", len(games))
    return games


def saveall(games):
    pass


class Game:
    def __init__(self, players, game_type=None, game_variant=None,
                 status="En Cours", creation_date=time.asctime()[4:], end_date=None):
        self.__players = players
        self.__game_type = game_type
        self.__game_variant = game_variant

        self.__status = status

        self.__creation_date = creation_date
        self.__end_date = end_date

    # TODO Generate Unique ID
    def save(self):
        main.GAMES[self.get_creation_date()] = self
        pass

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
