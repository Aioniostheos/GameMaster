import logging
import time
from pathlib import Path

import game
nom_fichier = Path("./data/logs/" + time.asctime().replace(":", "_") + " - debug.log")
fichier = nom_fichier.open('w+')
fichier.close()

logging.basicConfig(filename=nom_fichier, filemode="w", level=logging.DEBUG,
                    format='%(asctime)s %(name)s : %(levelname)s : %(message)s')
logger = logging.Logger("PyLog")

GAMES = []

if __name__ == "__main__":
    GAMES = game.load_all()
