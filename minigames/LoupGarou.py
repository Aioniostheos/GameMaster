from tkinter import *
from game import GameInfo
from typing import List
from player import Player
import logging
logger = logging.getLogger("PyLog")

class LoupGarou() :
    def __init__(self, players: List[Player]):
        super().__init__(players, GameInfo("Loup Garou", None))
        self.__app = None
        self.__morts=[]
        self.__vivants= List[Player]

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
    #sélectionner un rôle pour chaque joueur


    def options_Roles (self):
    #associer à chaque role ses caractéristiques : ex : une sorcière a deux potions


    def play_night (self, players, app):
    #à améliorer : appeler les joueurs dans l'odre en tenant compte de s'ils servent à quelque chose (sorcière sans potion ne sert à rien)
        tour1 = Label(app, text="Appeler le voleur")
        tour1.pack()
        app.mainloop()
        logger.info("Il n'apparait qu'au premier tour")
        tour1 = Label(app, text="Appeler Cupidon")
        tour1.pack()
        app.mainloop()
        logger.info("Il n'apparait qu'au premier tour et désigne deux amoureux")
        tour1 = Label(app, text="Appeler la voyante")
        tour1.pack()
        app.mainloop()
        logger.info("Elle choisit une carte à regarder")
        tour1 = Label(app, text="Appeler les loups garous, rappeler que la petite fille se réveille secrètement")
        tour1.pack()
        app.mainloop()
        logger.info("Ils tuent un joueur par nuit")
        tour1 = Label(app, text="Appeler la sorcière")
        tour1.pack()
        app.mainloop()
        logger.info("Elle a en tout deux potions : une sert à tuer, l'autre à revivre")

    def morts_NuitEtVotes (self, players, morts, vivants):
    #ajouter le(s) joueur(s) mort(s) dans la nuit et le joueur mort par vote à la liste morts et les enlever de la liste vivants


    def equipe_gagnante(self, players, vivants, app):
        m=0
        for player in vivants
            if player.role is not "Loups garous"
                m+=1
        if m==len(vivants) :
            alerte = LabelFrame(app, text="Résultats de la partie", padx=30, pady=30)
            alerte.pack(fill="both", expand="yes")
            Label(alerte, text="Les villageois ont gagné!").pack()
        if m==len(vivants)-1 and m==1 :
            alerte = LabelFrame(app, text="Résultats de la partie", padx=30, pady=30)
            alerte.pack(fill="both", expand="yes")
            Label(alerte, text="Les amoureux ont gagné!").pack()
        if m==0 :
            alerte = LabelFrame(app, text="Résultats de la partie", padx=30, pady=30)
            alerte.pack(fill="both", expand="yes")
            Label(alerte, text="Les loups garous ont gagné!").pack()


