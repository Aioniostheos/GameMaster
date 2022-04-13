# Pour chercher par mots clefs. Problèmes : ne reconnait pas le fichier + ce n est pas precis, donne des lignes mais pas la phrase concernee.

 def RechercheMotsclefs() :
   chaine = eval(input("Que recherchez-vous ? "))
   fichier = open('ReglesDesJeux','r')
   for l in fichier:
       if chaine in l:
           print (l-2,l-1,l,l+1,l+2)
   fichier.close()
   return
