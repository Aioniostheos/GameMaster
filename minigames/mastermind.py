import random
import tkinter as tk
from tkinter.ttk import Frame, Entry
from typing import Dict, List

from game import Game
from player import Player


class Mastermind(Game):
    @classmethod
    def load(cls, game_creation_date):
        pass

    def __init__(self, player, colorset: Dict[str, str] = None):
        super().__init__([player])
        if colorset is None:
            colorset = {"Rouge": "#AC0000", "Vert": "#00FF00", "Bleu": "#0000FF",
                        "Jaune": "#FFFF00", "Blanc": "#FFFFFF", "Noir": "#000000"}
        self.__lst_couleurs = list(colorset.values())
        self.__nb_coups = 0

        self.__solution = []
        self.__tentatives = [[] for i in range(12)]

    def get_solution(self):
        return self.__solution

    def get_nb_coups(self):
        return self.__nb_coups

    def get_couleurs(self):
        return self.__lst_couleurs

    def generer(self):
        self.__solution = []
        while len(self.__solution) < 4:
            couleur = random.choice(self.__lst_couleurs)
            self.__solution.append(couleur)

    @classmethod
    def start(cls):
        app = tk.Tk()
        app.title("Mastermind")
        app.geometry("175x175")

        entry = Entry(app)
        entry.pack()
        button = tk.Button(app, text="Jouer", command=lambda: [Mastermind(Player(entry.get())).play(app),
                                                               entry.pack_forget(), button.pack_forget()])
        button.pack()

        app.mainloop()

    def play(self, app):
        self.generer()
        app.geometry("175x400")
        frame = Frame(app)
        frame.pack(side=tk.BOTTOM, fill=tk.X)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(6, weight=1)

        history = Frame(app)
        history.pack(side=tk.TOP, fill=tk.X)
        history.grid_columnconfigure(0, weight=1)
        history.grid_columnconfigure(5, weight=1)
        history.grid_rowconfigure(0, weight=1)

        selection = []

        for i in range(1, 13):
            for j in range(1, 5):
                button = tk.Button(history, state=tk.DISABLED)
                self.__tentatives[i - 1].append(button)
                button.grid(row=i, column=j)

        for i in range(1, 5):
            button = tk.Button(frame, command=lambda: self.cycle_color(button))
            selection.append(button)
            button.grid(row=0, column=i)
        tk.Button(frame, text="Valider", command=lambda: self.attempt(selection)).grid(row=1, column=2, columnspan=3)

    def attempt(self, selection: List[tk.Button]):
        borders = []
        temp = self.__solution.copy()
        for i, button in enumerate(selection):
            if button.cget("bg") not in self.__lst_couleurs:
                pass
            if button.cget("bg") == self.__solution[i]:
                borders.append("red")
            elif button.cget("bg") in temp:
                temp.remove(button.cget("bg"))
                borders.append("white")
        for i, button in enumerate(self.__tentatives[self.__nb_coups]):
            button.config(bg=selection[i].cget("bg"), border=borders[i])
        self.__nb_coups += 1

    def cycle_color(self, button: tk.Button):
        if button.cget("bg") in self.__lst_couleurs:
            i = self.__lst_couleurs.index(button.cget("bg"))
            button.config(bg=self.__lst_couleurs[i + 1])
        else:
            button.config(bg=self.__lst_couleurs[0])
