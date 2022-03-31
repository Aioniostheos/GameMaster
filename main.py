import logging
import time
from pathlib import Path

import game

path = Path("./data/logs/" + time.asctime().replace(":", "_") + " - debug.log")
with path.open('w+') as file:
    pass

logging.basicConfig(filename=path, filemode="w", level=logging.DEBUG,
                    format='%(asctime)s %(name)s : %(levelname)s : %(message)s')
logger = logging.Logger("PyLog")

GAMES = []

if __name__ == "__main__":
    GAMES = game.load_all()
    print("Bienvenue")
    end = False
    while not end:
        print("Jouer (1)")
        print("Règle (2)")
        print("Quitter (3)")
        command = input()
        if command == '1':
            back = False
            while not back:
                print("Nouveau (1)")
                print("Charger (2)")
                print("Retour (3)")
                play = input()
                if play == '1':
                    print("Not Implemented")
                elif play == '2':
                    print("Not Implemented")
                elif play == '3':
                    back = True
                else:
                    print("Saisie non valide.\n")
        elif command == '2':
            print("Not Implemented")
        elif command == '3':
            end = True
        else:
            print("Saisie non valide.\n")
