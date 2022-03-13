import random as rd
import sys
sys.path.append('../GameMaster')
from GameMaster.game import Game

class Mastermind(Game):
    def __init__(self, Lst_colorset=["Rouge","Vert","Bleu","Jaune","Blanc","Noir"], Nb_cases=4,Nb_max_coups=12):
        self.__lst_couleurs = Lst_colorset
        self.__nb_cases = Nbcases
        self.__nb_max_coups = Nb_max_coups
        self.__nb_coup = 0

        self.__solution = []
        self.__lst_coups = []

    def get_solution(self):
        return self.__solution

    def get_nb_coup():
        return self.__nb_coup

    def generer(self):
        self.__solution = []
        while len(self.__solution)<= self.__nb_cases:
            self.__solution.append(rd.randint(0,len(self.__lst_couleurs)-1))

    def proposer(self,Proposition): #Proposition est une liste
        self.__lst_coups.append(Proposition)
        self.__nb_coup += 1

        lst_ret = []
        for i,couleur in enumerate(Proposition):
            if couleur == self.__solution[i]:
                lst_ret.append("Noir") #bonne couleur et bonne place
            else:
                if couleur in self.__solution:
                    lst_ret.append("Blanc") #bonne couleur, mauvaise place
        return lst_ret


if __name__ == '__main__':
    jeux = Mastermind()
    jeux.generer()
    print(jeux.get_solution())
