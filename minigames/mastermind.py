import random as rd
class Mastermind(Game):
    def __init__(self, Lst_colorset=["Rouge","Vert","Bleu","Jaune","Blanc","Noir"], Nb_cases=4,Nb_max_coups=12):
        self.__lst_couleurs = Lst_colorset
        self.__nb_cases = Nbcases
        self.__nb_max_coups = Nb_max_coups

        self.__solution = []

    def generer(self):
        self.__solution = []
        while len(self.__solution)<= self.__nb_cases:
            self.__solution.append(rd.randint(0,len(self.__lst_couleurs)-1))

    def get_solution(self):
        return self.__solution
