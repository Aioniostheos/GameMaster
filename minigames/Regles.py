from tkinter import *
#def RechercheMotsclefs() :
#  chaine = eval(input("Que recherchez-vous ? "))
#  fichier = open('ReglesDesJeux.docs','r')
#  for l in fichier:
#      if chaine in l:
#          print (l-2,l-1,l,l+1,l+2)
#  fichier.close()


class Regles():
    def __init__(self) :
        self.__app = None
    def start(self) :
        app = Tk()
        fichier = open('RegleDesJeux.docs','r')
        app.title("liste des règles")
        entry = Entry(app)
        entry.pack()
        Affichage = Label(app, text=fichier.read())
        Affichage.pack()
        app.mainloop()
        bouton = Button(app, text="Fermer", command=app.quit)
        bouton.pack()
