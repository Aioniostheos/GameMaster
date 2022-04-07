import logging
import time
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter.ttk import Button, Frame, Entry, Spinbox, Label

import game

GAMES = []

path = Path("./data/logs/" + time.asctime().replace(":", "_") + " - debug.log")
with path.open('w+') as file:
    pass

logging.basicConfig(filename=path, filemode="w", level=logging.DEBUG,
                    format='%(asctime)s %(name)s : %(levelname)s : %(message)s')
logger = logging.Logger("PyLog")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Master")
        logger.info("Initializing App")

        tabcontrol = ttk.Notebook(self)

        frame_gamemaster = ttk.Frame(tabcontrol)
        frame_minigames = ttk.Frame(tabcontrol)
        frame_rules = ttk.Frame(tabcontrol)

        Button(frame_minigames, width=10, text="Mastermind").pack()
        Button(frame_minigames, width=10, text="Bataille Navale").pack()

        tabcontrol.add(frame_gamemaster, text="Game Master")
        logger.info("Added \"Game Master\" tab")
        tabcontrol.add(frame_minigames, text="Mini-Jeux")
        logger.info("Added \"Mini-Jeux\" tab")
        tabcontrol.add(frame_rules, text="Règles")
        logger.info("Added \"Règles\" tab")
        tabcontrol.grid()

    def show(self):
        self.mainloop()
        logger.info("Showing App")


if __name__ == "__main__":
    logger = logging.getLogger("PyLog")
    GAMES = game.load_all()

    App().show()
