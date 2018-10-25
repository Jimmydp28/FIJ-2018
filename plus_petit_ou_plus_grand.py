#importe la librairie qui contient plusieurs fonctions aléatoire
import random 

#initialise nos différentes variable 
reponse = random.randrange(1,100)#on utilise la fonction randrange qui permet de choisir entre zero et le nombre entre () , ici 100
entree = -1
compteur = 10



while entree != reponse  and compteur > 0:# temps que la l'entrée est différente de la réponse et que le compteur est supérieur a zero ...

  entree = int( input("entre un nombre") )  #on change la valeur de " entrée " avec celle tapée au clavier . ATTENIONS , convertion en int

  if entree < reponse : 
    print ("la réponse est plus grande")
  elif entree > reponse :  #différencier If et Elif et Else 
    print ("la réponse est plus petite")
  else :
    print ("bravo,tu es un champion ")  

  compteur = compteur -1#attention a changé la valeur du compteur pour évité une boucle infinie 

  if compteur == 0 : 
    print (" You loose ! la réponse était :",reponse)
