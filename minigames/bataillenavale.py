import random as rd

from game import Game


class Bataillenavale(Game):
    def __init__(self, TailleGrille=10):
        self.__taille_grilles = TailleGrille

        self.__plateaux = [[["v" for i in range(TailleGrille)] for j in range(TailleGrille)] for k in range(2)]
        self.__tentatives = [[["v" for i in range(TailleGrille)] for j in range(TailleGrille)] for k in range(2)]

        self.__lst_bateaux = [[],[]]
        print(self.__lst_bateaux)
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

    def get_bateaux(self):
        return self.__lst_bateaux

    def set_bateau(self,joueur, coords1, coords2):
        try:
            joueur = int(joueur)-1
            ligne1 = self.__dico_lettres[coords1[0]]-1
            colone1 = int(coords1[1:])-1

            ligne2 = self.__dico_lettres[coords2[0]]-1
            colone2 = int(coords2[1:])-1
        except:
            return False

        ok_placer = True #valeur par défaut pour les testes de possibilitées de plassage après
        temp_lst = [] # pour append dans la liste des batteau
        if ligne1 == ligne2:
            cmin = min(colone1,colone2)
            cmax = max(colone1,colone2)

            for i in range (cmin,cmax+1): # test de possibilitées de plassage
                if self.__plateaux[joueur][ligne1][i] == "b":
                    ok_placer = False
            if ok_placer == True: # plassage
                for i in range (cmin,cmax+1):
                     self.__plateaux[joueur][ligne1][i] = "b"
                     temp_lst.append(str(ligne1)+str(i))
                self.__lst_bateaux[joueur].append(temp_lst)
                return True

        elif colone1 == colone2:
            lmin = min(ligne1,ligne2)
            lmax = max(ligne1,ligne2)

            for i in range (lmin,lmax+1): # test de possibilitées de plassage
                if self.__plateaux[joueur][i][colone1] == "b":
                    ok_placer = False
            if ok_placer == True: # plassage
                for i in range (lmin,lmax+1):
                     self.__plateaux[joueur][i][colone1] = "b"
                     temp_lst.append(str(i)+str(colone1))
                self.__lst_bateaux[joueur].append(temp_lst)
                return True

        return False


    def jouer(self, joueur, coords):  # joueur est celui qui joue
        try:
            ligne = self.__dico_lettres[coords[0]]-1
            colone = int(coords[1:])-1
            jatt = int(joueur)-1
            jdef = int(joueur)%2
        except:
            return False

        if self.__plateaux[jdef][ligne][colone] == "b": #ataque
            self.__tentatives[jatt][ligne][colone] = "t"
            self.__plateaux[jdef][ligne][colone] = "t"

            for lst_coords_bateau in self.__lst_bateaux[jdef]:  #detection de coullage de bateaux
                if (str(ligne)+str(colone)) in lst_coords_bateau:
                    touché = 0
                    for coords in lst_coords_bateau:
                        if self.__plateaux[jdef][int(coords[0])][int(coords[1])] == "t":
                            touché +=1
                    if touché == len(lst_coords_bateau):
                        for coords in lst_coords_bateau:
                            self.__plateaux[jdef][int(coords[0])][int(coords[1])] = "c"
                            self.__tentatives[jatt][int(coords[0])][int(coords[1])] = "c"

            return True

        elif self.__plateaux[jdef][ligne][colone] == "t":
            return False
        else:
            self.__tentatives[jatt][ligne][colone] = "m"
            self.__plateaux[jdef][ligne][colone] = "m"
            return  True
