import logging
import time

import game
nom_fichier = "./data/logs/" + time.asctime().replace(":", "_") + " - debug.log"
fichier = open(nom_fichier,'w+')
fichier.close()

logging.basicConfig(filename=nom_fichier, filemode="w", level=logging.DEBUG,
                    format='%(asctime)s %(name)s : %(levelname)s : %(message)s')
logger = logging.Logger("PyLog")

GAMES = []

if __name__ == "__main__":
    GAMES = game.load_all()
