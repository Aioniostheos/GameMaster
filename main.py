import logging
import time
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter.ttk import Button

GAMES = {}

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

        Button(frame_minigames, text="Mastermind", command=lambda: startMastermind()).pack()
        Button(frame_minigames, text="Bataille Navale").pack()

        tabcontrol.add(frame_gamemaster, text="Game Master")
        logger.info("Added \"Game Master\" tab")
        tabcontrol.add(frame_minigames, text="Mini-Jeux")
        logger.info("Added \"Mini-Jeux\" tab")
        tabcontrol.add(frame_rules, text="Règles")
        logger.info("Added \"Règles\" tab")
        tabcontrol.grid()

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    import game
    from minigames.mastermind import Mastermind
    logger = logging.getLogger("PyLog")
    GAMES = game.load_all()

    def startMastermind():
        Mastermind.start()

    app = App()

    def on_closing():
        game.save_all(GAMES)
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.show()
