from random import *

prix_just = randint(1,1000)
Réussi = False 
Tentative = 0
while Réussi == False : 
    prix = int(input("Quelle est le prix de l'objet vous penser "))
    
    if Tentative >= 20 :
        print ("Tu a pris trop de temps , réassaye la prochaine fois")
        break
    else :
        pass 
    
    if prix == prix_just :
        Réussi == True
        print ("Bravo, Vous avez réussi a trouvez le juste prix qui étais", prix_just) 
        break
    elif prix < prix_just :
        print ("C'est plus")
        Tentative += 1
    elif prix > prix_just :
        print ("C'est moins")
        Tentative += 1

terminate = input ()
