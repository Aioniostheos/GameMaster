import logging
import time
from pathlib import Path
from tkinter.ttk import Frame
from typing import List, Dict
from xml.etree import ElementTree

import main
from player import Player

logger = logging.getLogger("PyLog")


class GameInfo:
    def __init__(self, type, variant, status="En Cours", creation_date: str = time.asctime()[4:], end_date: str = "", filepath: str = ""):
        self.type = type
        self.variant = variant
        self.status = status
        self.creation_date = creation_date
        self.end_date = end_date
        self.filepath = Path(filepath)


class Game:
    def __init__(self, players: List[Player], gameinfo=GameInfo(None, None)):
        self.__players = players
        self.__game_type = gameinfo.type
        self.__game_variant = gameinfo.variant

        self.__status = gameinfo.status
        self.__filepath = gameinfo.filepath

        self.__creation_date = gameinfo.creation_date
        self.__end_date = gameinfo.end_date

        self.frame = None

    @classmethod
    def load(cls, game_creation_date):
        raise NotImplementedError()

    # TODO Generate Unique ID
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
        return self.__game_type

    def get_game_variant(self):
        return self.__game_variant

    def get_creation_date(self):
        return self.__creation_date

    def get_end_date(self):
        return self.__end_date

    def get_filepath(self):
        return self.__filepath

    def get_players(self):
        return self.__players

    def get_players_with(self, prop: str, value: object):
        return [player for player in self.__players if player.get(prop) == value]

    def get_status(self):
        return self.__status

    @classmethod
    def start(cls):
        raise NotImplementedError()


def load_all() -> Dict[str, Game]:
    games = {}
    path = Path("data/saves/games.xml")
    if not path.exists():
        logger.info("No game save")
        pass
    with path.open() as file:
        root = ElementTree.parse(file).getroot()
        if root.tag != "games":
            logger.warning("Corrupted file: %s", path.name)
            pass
        game_elements = root.findall("game")
        logger.info("Find %s game saves", len(game_elements))
        for game_element in game_elements:
            players = []
            for player_element in game_element.findall("player"):
                player_name = player_element.attrib["name"]
                player_properties = {}
                for prop in player_element:
                    player_properties[prop.tag] = prop.text
                players.append(Player(player_name, player_properties))
            games[game_element.attrib["creation_date"]] = Game(players,
                GameInfo(game_element.attrib["type"], game_element.attrib["variant"], game_element.attrib["status"],
                    game_element.attrib["creation_date"], game_element.attrib["end_date"], game_element.attrib["filepath"]))
    return games


def save_all(games: Dict[str, Game]):
    root = ElementTree.Element("games")
    for game in games.values():
        game_element = ElementTree.Element("game")
        game_element.attrib["type"] = game.get_game_type()
        game_element.attrib["variant"] = game.get_game_variant()
        game_element.attrib["status"] = game.get_status()
        game_element.attrib["creation_date"] = game.get_creation_date()
        game_element.attrib["end_date"] = game.get_end_date()
        game_element.attrib["filepath"] = game.get_filepath()

        root.append(game_element)
        for player in game.get_players():
            player_element = ElementTree.SubElement(game_element, "player")
            player_element.attrib["name"] = player.getName()
            for prop, value in player.getProperties():
                prop_element = ElementTree.SubElement(player_element, "prop")
                prop_element.text = value

    tree = ElementTree.ElementTree(root)
    ElementTree.indent(tree, space="\t", level=0)
    tree.write("data/saves/games.xml", encoding="utf-8")
