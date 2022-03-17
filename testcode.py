import time as T
from game import Game
from minigames.mastermind import Mastermind
from minigames.bataillenavale import Bataillenavale

I = 2


if __name__ == '__main__':
    if I == 1:
        jeux = Mastermind()
        jeux.generer()
        print("solution : ",jeux.get_solution())

        dicopropo = {"R":"Rouge","G":"Vert","B":"Bleu","Y":"Jaune","W":"Blanc","D":"Noir"}
        run = True
        while run:
            okin =False
            while not okin:
                entré = input("proposition :")
                if len(entré) == len(jeux.get_solution()):
                        okin = True
            lst_out = []
            for lettre in entré:
                lst_out.append(dicopropo[lettre.upper()])
            sortie = jeux.proposer(lst_out)
            print(sortie)


    elif I == 2:
        jeux = Bataillenavale()

        lst_lettres = ["A","B","C","D","E","F","G","H","I","J"]

        run = True
        while run:
            plateau1 = jeux.get_plateau(1)
            plateau2 = jeux.get_plateau(2)
            tentatives1 = jeux.get_tentatives(1)
            tentatives2 = jeux.get_tentatives(2)

            print(len(plateau1[1]))
            print(len(plateau1))
            print("")

            print("|joueur 1 : tentatives|          |joueur 2 : tentatives|")
            print("|---------------------|          |---------------------|")
            print("||1 2 3 4 5 6 7 8 9 10|          ||1 2 3 4 5 6 7 8 9 10|")
            for i,lettre in enumerate(lst_lettres):
                str = lettre +"|"
                for j in range(10):
                    str+= (tentatives1[i][j]+" ")
                str += "|          "+lettre+"|"
                for j in range(10):
                    str+= (tentatives2[i][j]+" ")
                str += "|"
                print(str)
            print("")
            print("|joueur 1 : plateau   |          |joueur 2 : plateau   |")
            print("|---------------------|          |---------------------|")
            print("||1 2 3 4 5 6 7 8 9 10|          ||1 2 3 4 5 6 7 8 9 10|")
            for i,lettre in enumerate(lst_lettres):
                str = lettre +"|"
                for j in range(10):
                    str+= (plateau1[i][j]+" ")
                str += "|          "+lettre+"|"
                for j in range(10):
                    str+= (plateau2[i][j]+" ")
                str += "|"
                print(str)

            print("")
            print("format des entrés : action ; joueur ; coords ( ; direction ; taille si set)")
            print("action : [A/B] ; attaque / bateau ")
            print("joueur : [1/2] ; joueur qui fait l'action ")
            print("coords : [A-J/1-10] ; format lettre chiffre")
            print("dirrection : [H/B/G/D] sens du bateau")
            entre = input("action ? :")
            lst_entre = entre.split(";")

            if lst_entre[0] == "B":
                if len(lst_entre) == 5:
                    OK = jeux.set_bateau(lst_entre[1],lst_entre[2],lst_entre[3],int(lst_entre[4]))
                    print(OK)
