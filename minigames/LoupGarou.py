from tkinter import *
from game import GameInfo
from typing import List
from player import Player

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


    def play_night (self, players):
    #à améliorer : appeler les joueurs dans l'odre en tenant compte de s'ils servent à quelque chose (sorcière sans potion ne sert à rien)
    tour = Label(app, text="appeler le voleur")
    tour.pack()
    app.mainloop()
    logger.info("Starting game...")

    def morts_NuitEtVotes (self, players, morts, vivants):
    #ajouter le(s) joueur(s) mort(s) dans la nuit et le joueur mort par vote à la liste morts et les enlever de la liste vivants


    def equipe_gagnante(self, players, vivants):
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


