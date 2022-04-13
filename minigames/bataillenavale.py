import logging
import random as rd
import tkinter as tk

from game import Game, GameInfo
from player import Player
from tkinter import messagebox
from tkinter.ttk import Frame, Entry, Label
from typing import List

logger = logging.getLogger("PyLog")


class BatailleNavale(Game):
    def __init__(self, players: List[Player], TailleGrille=10):
        super().__init__(players, GameInfo("Bataille Navale", None))
        self.__taille_grilles = TailleGrille
        self.__click = tk.IntVar(value=0)
        self.__coords = ()

        for player in players:
            player.with_property("plateau", [["#0000FF" for i in range(TailleGrille)] for j in range(TailleGrille)])
            player.with_property("tentatives", [["#000000" for i in range(TailleGrille)] for j in range(TailleGrille)])
            player.with_property("bateaux", [])

        self.__app = None
        self.__frame = Frame()

    def set_bateau(self, player: Player, x1, y1, x2, y2):
        bateau = []
        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)

            for i in range(y_min, y_max + 1):
                if player.get("plateau")[x1][i] == "#ACACAC":
                    return

            for i in range(y_min, y_max + 1):
                player.get("plateau")[x1][i] = "#ACACAC"
                bateau.append((x1, i))
            player.get("bateaux").append(bateau)

        elif y1 == y2:
            x_min = min(x1, x2)
            x_max = max(x1, x2)

            for i in range(x_min, x_max + 1):
                if player.get("plateau")[i][y1] == "#ACACAC":
                    return
            for i in range(x_min, x_max + 1):
                player.get("plateau")[i][y1] = "#ACACAC"
                bateau.append((i, y1))
            player.get("bateaux").append(bateau)

    @classmethod
    def start(cls):
        app = tk.Tk()
        app.title("Bataille Navale")
        logger.info("Starting Bataille Navale...")
        frame = Frame(app)
        frame.pack()
        Label(frame, text="J1: ").pack(side=tk.LEFT)
        entry_J1 = Entry(frame)
        entry_J1.pack(side=tk.LEFT)
        entry_J2 = Entry(frame)
        entry_J2.pack(side=tk.RIGHT)
        Label(frame, text="J2: ").pack(side=tk.RIGHT)
        button = tk.Button(frame, text="Jouer", command=lambda: [frame.pack_forget(),
                                                                 BatailleNavale([Player(entry_J1.get()), Player(entry_J2.get())]).play(app)])
        button.pack(side=tk.BOTTOM)

        app.mainloop()

    def play(self, app: tk.Tk):
        self.__app = app
        self.start_placement(1)

    def start_placement(self, player_number):
        if player_number > 2:
            self.turn(player_number % 2)
            return
        self.__frame.pack_forget()
        self.__frame = Frame(self.__app)
        self.__frame.pack()
        Label(self.__frame, text="J" + str(player_number)).pack()
        Label(self.__frame, text="Placement des Bateaux").pack()
        plateau = Frame(self.__frame)
        plateau.pack()
        plateau.grid_columnconfigure(0, weight=1)
        plateau.grid_columnconfigure(self.__taille_grilles + 2, weight=1)

        for x in range(self.__taille_grilles):
            Label(plateau, text=x + 1).grid(row=x + 1, column=1)
        for y in range(self.__taille_grilles):
            Label(plateau, text=y + 1).grid(row=0, column=y + 2)

        for x in range(self.__taille_grilles):
            for y in range(self.__taille_grilles):
                button = tk.Button(plateau, bg=self.get_players()[player_number - 1].get("plateau")[x][y], width=5, height=2,
                                   command=lambda row=x, column=y: [self.__click.set((self.__click.get() + 1) % 2), self.button_click(player_number, row, column)])
                button.grid(row=x + 1, column=y + 2)

        done = tk.Button(self.__frame, text="Terminer", command=lambda: [self.start_placement(player_number + 1)])
        done.pack()

    def button_click(self, player_number, x, y):
        if self.__click.get() == 1:
            self.__coords = (x, y)
        else:
            self.set_bateau(self.get_players()[player_number - 1], self.__coords[0], self.__coords[1], x, y)
            self.start_placement(player_number)

    def turn(self, player_number):
        self.__frame.pack_forget()
        self.__frame = Frame(self.__app)
        self.__frame.pack()
        Label(self.__frame, text="J" + str(player_number)).pack()

        tentatives = Frame(self.__frame)
        tentatives.pack()
        tentatives.grid_columnconfigure(0, weight=1)
        tentatives.grid_columnconfigure(self.__taille_grilles + 2, weight=1)

        for x in range(self.__taille_grilles):
            Label(tentatives, text=x + 1).grid(row=x + 1, column=1)
        for y in range(self.__taille_grilles):
            Label(tentatives, text=y + 1).grid(row=0, column=y + 2)

        for x in range(self.__taille_grilles):
            for y in range(self.__taille_grilles):
                button = tk.Button(tentatives, bg=self.get_players()[player_number - 1].get("tentatives")[x][y], width=5, height=2,
                                   command=lambda row=x, column=y: self.shoot(player_number, row, column))
                button.grid(row=x + 1, column=y + 2)

        plateau = Frame(self.__frame)
        plateau.pack()
        plateau.grid_columnconfigure(0, weight=1)
        plateau.grid_columnconfigure(self.__taille_grilles + 2, weight=1)

        for x in range(self.__taille_grilles):
            Label(plateau, text=x + 1).grid(row=x + 1, column=1)
        for y in range(self.__taille_grilles):
            Label(plateau, text=y + 1).grid(row=0, column=y + 2)

        for x in range(self.__taille_grilles):
            for y in range(self.__taille_grilles):
                button = tk.Button(plateau, bg=self.get_players()[player_number - 1].get("plateau")[x][y], width=5, height=2, state=tk.DISABLED)
                button.grid(row=x + 1, column=y + 2)

    def shoot(self, player_number, x, y):
        attacker = self.get_players()[player_number - 1]
        defender = self.get_players()[player_number % 2]
        sunk = False
        sunks = 0
        if defender.get("plateau")[x][y] == "#ACACAC":
            attacker.get("tentatives")[x][y] = "#AC0000"
            defender.get("plateau")[x][y] = "#AC0000"
            for bateau in defender.get("bateaux"):
                if (x, y) in bateau:
                    bateau.remove((x,y))
                    print(bateau)
                if len(bateau) == 0:
                    sunk = True
                    sunks += 1

            if sunks == len(defender.get("bateaux")):
                res = tk.messagebox.askretrycancel(title="Félicitations", message="J"
                + str(player_number) + " a gagné ! Voulez-vous rejouer ?", parent=self.__app)
                if res:
                    self.__app.destroy()
                    BatailleNavale.start()
                else:
                    self.__app.destroy()
                self.end()
                logger.info("Game marked as ended.")
                self.save()
                logger.info("Game saved.")
            elif sunk:
                tk.messagebox.showinfo(message="Touché-Coulé ! Vous pouvez rejouer !", parent=self.__app)
            else:
                tk.messagebox.showinfo(message="Touché ! Vous pouvez rejouer !", parent=self.__app)
            self.turn(player_number)

        elif defender.get("plateau")[x][y] != "#AC0000":
            tk.messagebox.showinfo(message="A l'eau ! C'est à votre adversaire !", parent=self.__app)
            attacker.get("tentatives")[x][y] = "#0000FF"
            defender.get("plateau")[x][y] = "#0000AC"
            self.turn((player_number + 1) % 2)
