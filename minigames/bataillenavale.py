import random as rd

from game import Game


class Bataillenavale(Game):
    def __init__(self, TailleGrille=10):
        self.__taille_grilles = TailleGrille

        # temp_lst1 = []
        # temp_lst2 = []
        # while len(temp_lst1) < self.__taille_grilles:
        #     temp_lst1.append("v")
        # while len(temp_lst2) < self.__taille_grilles:
        #     temp_lst2.append(temp_lst1[:])
        # self.__plateaux = []
        # self.__plateaux.append(temp_lst2[:])
        # self.__plateaux.append(temp_lst2[:])
        # self.__tentatives = []
        # self.__tentatives.append(temp_lst2[:])
        # self.__tentatives.append(temp_lst2[:])
        self.__plateaux = [[["v"]*10]*10]*2
        self.__tentatives = [[["v"]*10]*10]*2
        """
        |
        |   /!\ problème d'adresses mémoires, les 2 plateau et les 2 tentatives ont les mêmes listes
        |
        """

        self.__dico_lettres = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
                               "J": 10}  # coords en format lettre-chiffre

    def get_plateau(self, joueur):
        joueur = int(joueur)
        return self.__plateaux[joueur - 1]

    def get_tentatives(self, joueur):
        joueur = int(joueur)
        return self.__tentatives[joueur - 1]

    def set_bateau(self, joueur, coords, direction, taille):  # direction est un str : {"H","B","G","D"}
        print(joueur,coords,direction,taille)
        ligne = self.__dico_lettres[coords[0]]-1
        colone = int(coords[1])-1
        joueur = int(joueur)
        cases_ok = 0
        for i in range(taille):
            try:
                if direction == "H":
                    if self.__plateaux[joueur - 1][ligne - i][colone] == "v":
                        cases_ok += 1
                if direction == "B":
                    if self.__plateaux[joueur - 1][ligne + i][colone] == "v":
                        cases_ok += 1
                if direction == "G":
                    if self.__plateaux[joueur - 1][ligne][colone - i] == "v":
                        cases_ok += 1
                if direction == "D":
                    if self.__plateaux[joueur - 1][ligne][colone + i] == "v":
                        cases_ok += 1
            except:
                pass

        if cases_ok == taille:
            for i in range(taille):
                if direction == "H":
                    self.__plateaux[joueur - 1][ligne - i][colone] = "b"
                if direction == "B":
                    self.__plateaux[joueur - 1][ligne + i][colone] = "b"
                if direction == "G":
                    self.__plateaux[joueur - 1][ligne][colone - i] = "b"
                if direction == "D":
                    self.__plateaux[joueur - 1][ligne][colone + i] = "b"
            return True

        return False  # cas ou le set n'a pas pue se faire

    def jouer(self, joueur, coords):  # joueur est celui qui joue
        ligne = self.__dico_lettres[coords[0]]
        colone = int(coords[1])-1
        joueur = int(joueur)-1

        if self.__plateaux[joueur % 2][ligne][colone] == "b":
            self.__tentatives[joueur - 1][ligne][colone] = "t"
            self.__plateaux[joueur % 2][ligne][colone] = "t"

            if self.__plateaux[joueur % 2][ligne - 1][colone] == "t":
                pass
                """
                |
                |   /!\ à faire : detection de coullage de bateau (passage des cases en "c")
                |
                """

        else:
            self.__tentatives[joueur - 1][ligne][colone] = "m"
