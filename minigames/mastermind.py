import random as rd

from game import Game

class Mastermind(Game):
    def __init__(self, Lst_colorset=["Rouge","Vert","Bleu","Jaune","Blanc","Noir"], Nb_cases=4,Nb_max_coups=12):
        self.__lst_couleurs = Lst_colorset
        self.__nb_cases = Nb_cases
        self.__nb_max_coups = Nb_max_coups
        self.__nb_coup = 0

        self.__solution = []
        self.__lst_coups = []

    def get_solution(self):
        return self.__solution

    def get_nb_coup():
        return self.__nb_coup

    def get_couleurs():
        return self.__lst_couleurs

    def get_coups():
        return self.__lst_coups

    def generer(self):
        self.__solution = []
        while len(self.__solution)< self.__nb_cases:
            couleur = self.__lst_couleurs[rd.randint(0,len(self.__lst_couleurs)-1)]
            self.__solution.append(couleur)

    def proposer(self,Proposition): #Proposition est une liste
        self.__lst_coups.append(Proposition)
        self.__nb_coup += 1
        """
        |
        |       /!\ A VOIR : COMMENT GERER LA PRESENCE MULTIPLE D'UNE MEME COULEUR
        |
        """
        lst_ret = []
        for i,couleur in enumerate(Proposition):
            if couleur == self.__solution[i]: #bonne couleur et bonne place
                lst_ret.append("Noir")
            else:
                if couleur in self.__solution:
                    lst_ret.append("Blanc") #bonne couleur, mauvaise place
        return lst_ret
