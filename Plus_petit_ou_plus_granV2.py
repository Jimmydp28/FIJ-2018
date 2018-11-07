import random

reponse = "o"
while reponse == "o" :
  nombre_a_trouver  = random.randrange(100)


  compteur = 10

  entree = -1

  while entree != nombre_a_trouver and compteur > 0 :
    entree = int (input("tapez un nombre "))

    if entree < nombre_a_trouver : 
      compteur -=1
      print ( " le nombre est plus petit que la reponse , essaie restant :", compteur)
    elif entree > nombre_a_trouver : 
      compteur -=1
      print ( " le nombre est plus grand que la réponse essaie restant :", compteur)
    else  : 
      print ( " tu as trouvé " )
    


  if compteur == 0 :
    print ("perdu c'était",nombre_a_trouver )

  reponse = input("voulez vous rejoué ?o/n")
