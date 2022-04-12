from player import Player
from main import game


def getPlayerStats(pPlayer: Player):
    nomPlayer = pPlayer.getName()
    statsPlayer = pPlayer.get("Statitics")
    return nomPlayer, statsPlayer


def show(pPlayer: Player):
    Nom, Stats = getPlayerStats(pPlayer)
