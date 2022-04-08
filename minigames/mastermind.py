import random
import tkinter as tk
from tkinter import messagebox
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

        self.__app = None

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
        self.__app = app
        self.generer()
        app.geometry("250x575")
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
                button = tk.Button(history, width=5, height=2)
                self.__tentatives[i - 1].append(button)
                button.grid(row=i, column=j)

        b1 = tk.Button(frame, width=5, height=2, command=lambda: self.cycle_color(b1))
        b2 = tk.Button(frame, width=5, height=2, command=lambda: self.cycle_color(b2))
        b3 = tk.Button(frame, width=5, height=2, command=lambda: self.cycle_color(b3))
        b4 = tk.Button(frame, width=5, height=2, command=lambda: self.cycle_color(b4))

        selection.append(b1)
        selection.append(b2)
        selection.append(b3)
        selection.append(b4)

        b1.grid(row=0, column=1)
        b2.grid(row=0, column=2)
        b3.grid(row=0, column=3)
        b4.grid(row=0, column=4)

        tk.Button(frame, text="Valider", width=10, command=lambda: self.attempt(selection)).grid(row=1, column=3, columnspan=2)

    def attempt(self, selection: List[tk.Button]):
        color = []
        temp = self.__solution.copy()
        correct = 0
        for i, button in enumerate(selection):
            if button.cget("bg") not in self.__lst_couleurs:
                pass
            if button.cget("bg") == self.__solution[i]:
                temp.remove(button.cget("bg"))
                color.append("red")
                correct += 1
            elif button.cget("bg") in temp:
                temp.remove(button.cget("bg"))
                color.append("white")
            else:
                color.append("black")
        for i, button in enumerate(self.__tentatives[self.__nb_coups]):
            button.config(bg=selection[i].cget("bg"), activebackground=color[i])
        self.__nb_coups += 1
        if correct >= 4:
            res = tk.messagebox.askretrycancel(title="Félicitations", message="Vous avez gagné ! ("
            + str(self.__nb_coups) + " coups)", parent=self.__app)
            if res:
                self.__app.destroy()
                Mastermind.start()
            else:
                self.__app.destroy()
            self.get_players()[0].get("Statitics").append(["Victory", self.__nb_coups])
        if self.__nb_coups == 12:
            res = tk.messagebox.askretrycancel(title="Dommage...", message="Vous avez perdu...", parent=self.__app)
            if res:
                self.__app.destroy()
                Mastermind.start()
            else:
                self.__app.destroy()
            self.get_players()[0].get("Statitics").append(["Defeat", self.__nb_coups])

    def cycle_color(self, button: tk.Button):
        if button.cget("bg") in self.__lst_couleurs:
            i = self.__lst_couleurs.index(button.cget("bg"))
            if i + 1 < len(self.__lst_couleurs):
                button.config(bg=self.__lst_couleurs[i + 1])
            else:
                button.config(bg=self.__lst_couleurs[0])
        else:
            button.config(bg=self.__lst_couleurs[0])
