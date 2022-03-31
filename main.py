import logging
import game

logging.basicConfig(filename="./data/logs/debug.log", filemode="w", level=logging.DEBUG,
                    format='%(asctime)s %(name)s : %(levelname)s : %(message)s')
logger = logging.Logger("PyLog")

GAMES = []

if __name__ == "__main__":
    GAMES = game.load_all()
