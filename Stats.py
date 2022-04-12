import main
from player import Player


def getPlayerStats(pPlayer: Player):
    nomPlayer = pPlayer.getName()
    statsPlayer = pPlayer.get("Statitics")
    return nomPlayer, statsPlayer


def getAmount(game_type: str):
    i = 0
    for gameinfo in main.GAMES.values():
        if gameinfo.type == game_type:
            i += 1
    return i


def show(pPlayer: Player):
    Nom, Stats = getPlayerStats(pPlayer)
