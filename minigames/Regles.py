logger = logging.getLogger("PyLog")
 def RechercheMotsclefs() :
   chaine = eval(input("Que recherchez-vous ? "))
   fichier = open('ReglesDesJeux.docs','r')
   for l in fichier:
       if chaine in l:
           print (l-2,l-1,l,l+1,l+2)
   fichier.close()
   return

class Regles()
    def afficher
        app = tk.Tk()
        app.title("liste des règles")
        entry = Entry(app)
        entry.pack()
        Affichage = Label(app, text=open('RegledDesJeux.docs',r))
        Affichage.pack()
        fenetre.mainloop()
        bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
        bouton.pack()
