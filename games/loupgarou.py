import logging

import tkinter as tk

from game import Game, GameInfo
from player import Player
from tkinter.ttk import Combobox, Label, Entry, Frame
from typing import List

logger = logging.getLogger("PyLog")

roles = ["Loup-Garou", "Grand-Méchant-Loup", "L'Infect Père des Loups", "Voleur", "Servante Dévouée", "Comédien", "Enfant Sauvage", "Chien-Loup",
         "Villageois", "Villageois-Villageois", "Voyante", "Cupidon", "Sorcière", "Chasseur", "Petite Fille", "Salvateur", "L'Ancien", "Bouc Emissaire",
         "Idiot", "2 Soeurs", "3 Frères", "Renard", "Montreur d'Ours", "Juge Bègue", "Chevalier à l'Epée Rouillée", "Pyromane", "Corbeau", "Gitane",
         "Garde Champêtre", "Loup-Garou Blanc", "Ange", "Joueur de Flûte", "Abominable Sectaire"]

class LoupGarou(Game):
    def __init__(self, entries: List[Entry]):
        players = []
        for entry in entries:
            players.append(Player(entry.get()))
        super().__init__(players, GameInfo("Loup-Garou", None))

        self.__app = None
        self.__frame = None
        self.__married_1 = None

    @classmethod
    def start(cls):
        app = tk.Tk()
        app.title("Loup-Garou")
        logger.info("Starting Loup-Garou GM...")
        frame = Frame(app)
        frame.pack()
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        entries = []
        entry1 = Entry(frame)
        entries.append(entry1)
        entry1.grid(row=1, column=1)

        i = tk.IntVar(value=2)
        add = tk.Button(frame, text="+", width=2, fg="green", command=lambda: [add_player(frame, entries, add, i), i.set(i.get() + 1)])
        add.grid(row=i.get(), column=2)

        button = tk.Button(frame, text="Valider", command=lambda: [frame.pack_forget(), LoupGarou(entries).select_roles(app)])
        button.grid(row=0, column=1)

        app.mainloop()

    def select_roles(self, app):
        self.__app = app
        self.__frame = Frame(app)
        self.__frame.pack()
        self.__frame.grid_columnconfigure(0, weight=1)
        self.__frame.grid_columnconfigure(3, weight=1)

        role_selectors = []

        for i, player in enumerate(self.get_players()):
            Label(self.__frame, text=player.getName()).grid(row=i, column=1)
            role_selector = Combobox(self.__frame, values=roles)
            role_selectors.append(role_selector)
            role_selector.grid(row=i, column=2)

        button = tk.Button(self.__frame, text="Jouer", command=lambda: [self.__frame.pack_forget(), self.set_roles(role_selectors), self.play()])
        button.grid(row=len(self.get_players()), column=1, columnspan=2)

    def set_roles(self, selectors: List[Combobox]):
        for player, selector in zip(self.get_players(), selectors):
            player.with_property("role", selector.get())

    def play(self):
        self.refresh()

    def refresh(self):
        self.__frame.pack_forget()
        self.__frame = Frame(self.__app)
        self.__frame.pack()
        buttons = Frame(self.__frame)
        buttons.pack(side=tk.TOP)
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(3, weight=1)
        tk.Button(buttons, text="Appeler", command=lambda: self.call()).grid(row=0, column=1)
        tk.Button(buttons, text="Eliminer", command=lambda: self.kill()).grid(row=0, column=2)
        tk.Button(buttons, text="Marier", command=lambda: self.marry()).grid(row=0, column=3)
        tk.Button(buttons, text="Elire", command=lambda: self.vote()).grid(row=0, column=4)

        for player in self.get_players():
            button = tk.Button(self.__frame, text=player.getName(), command=lambda p=player: tk.messagebox.showinfo(title=p.getName(), message="Rôle : " + p.get("role")
                        + "\r\nStatut :\r\n\tMarié(e) : " + str(p.get("married")) + "\r\n\tMaire : " + str(p.get("mayor")), parent=self.__app))
            if player.get("dead") is not None:
                button.config(state=tk.DISABLED, bg="#BCBCBC")
            button.pack()

    def call(self):
        call_tk = tk.Tk()
        role = Combobox(call_tk, values=roles)
        role.pack()
        tk.Button(call_tk, text="Appeler", command=lambda: [call_tk.destroy(), tk.messagebox.showinfo(title=role.get(), message=self.show_players_with("role", role.get()), parent=self.__app),
                                                            self.refresh()]).pack()

    def kill(self):
        kill_tk = tk.Tk()
        for player in self.get_players():
            tk.Button(kill_tk, text=player.getName(), command=lambda p=player: [kill_tk.destroy(), p.set("dead", True), self.kill_married(p),
                                                                                tk.messagebox.showinfo(title="Décès", message=p.getName() + " est décédé !", parent=self.__app),
                                                                                self.refresh()]).pack()

    def kill_married(self, player):
        if player.get("married") is not None:
            p2 = player.get("married")
            p2.set("dead", True)
            tk.messagebox.showinfo(title="Décès", message=p2.getName() + " est décédé !", parent=self.__app)

    def marry(self):
        marry_tk = tk.Tk()
        for player in self.get_players():
            tk.Button(marry_tk, text=player.getName(), command=lambda p=player: self.marry_click(marry_tk, p)).pack()

    def marry_click(self, marry_tk, player):
        if self.__married_1 is not None:
            marry_tk.destroy()
            self.__married_1.set("married", player)
            player.set("married", self.__married_1)
            tk.messagebox.showinfo(title="Mariage", message="Félicitations à " + self.__married_1.getName() + " et " + player.getName() + " pour leur mariage !", parent=self.__app)
        else:
            self.__married_1 = player

    def vote(self):
        vote_tk = tk.Tk()
        for player in self.get_players():
            tk.Button(vote_tk, text=player.getName(), command=lambda p=player: [vote_tk.destroy(), p.set("mayor", True),
                      tk.messagebox.showinfo(title="Elections", message=p.getName() + " est le nouveau maire !", parent=self.__app), self.refresh()]).pack()


def add_player(frame: Frame, entries: List[Entry], add: tk.Button, i):
    entry = Entry(frame)
    entries.append(entry)
    entry.grid(row=i.get(), column=1)
    remove = tk.Button(frame, text="-", width=2, fg="red", command=lambda: [i.set(i.get() - 1), remove_player(entries, entry, remove, add, i)])
    remove.grid(row=i.get(), column=2)
    add.grid_forget()
    add.grid(row=i.get() + 1, column=2)


def remove_player(entries: List[Entry], entry: Entry, remove: tk.Button, add: tk.Button, i):
    entries.pop()
    entry.grid_forget()
    remove.grid_forget()
    add.grid_forget()
    add.grid(row=i.get(), column=2)
