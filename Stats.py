from player import Player
from main import game


def getPlayerStats(pPlayer: Player):
    nomPlayer = pPlayer.getName()
    statsPlayer = pPlayer.getProperties()
    return nomPlayer, statsPlayer


def show(pPlayer: Player):
    Nom, Stats = getPlayerStats(pPlayer)