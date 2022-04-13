from tkinter import *
from game import GameInfo
from typing import List
from player import Player

class LoupGarou() :
    def __init__(self, players: List[Player]):
        super().__init__(players, GameInfo("Bataille Navale", None))
        self.__app = None
        self.__morts=[]

    def listRoles (self):
        app = Tk()
        listeDesRoles = Listbox(app)
        listeDesRoles.insert(1, "Loups garous")
        listeDesRoles.insert(2, "Simples Villageois")
        listeDesRoles.insert(3, "Voyante")
        listeDesRoles.insert(4, "Sorcière")
        listeDesRoles.insert(5, "Cupidon")
        listeDesRoles.insert(6, "Chasseur")
        listeDesRoles.insert(7, "Voleur")
        listeDesRoles.insert(8, "Petite fille")
        listeDesRoles.pack()

    def association(self,listeDesRoles,players):


    def options_Roles (self):


    def play_night (self, players):


    def morts_NuitEtVotes (self, players, morts):


