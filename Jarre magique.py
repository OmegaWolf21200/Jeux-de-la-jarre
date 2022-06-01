from random import randint


print ("Bienvenue dans le jeux")
print ("Vous deverez Trouvez trois fois de suite une clef dans chaque jarre")
cle = 0
Dif = int(input("Quelle lvl de difficulter (Entre 1 et 3)"))

while cle != 3 and Dif == 1 :
    if cle == 3 :
        break 

    if cle < 0 :
        cle = 0
    Serpant = randint (1, 5)

    Jarre = input("Choisissez quelle jarre vous voullez mettre la main (1 à 5) : ")

    if int(Jarre) == Serpant :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) > 5 :
        print ("Vous avez mis un nombre superieur a 5, recommencez")
    
    else :
        cle += 1
        print ("Piouff , vous avez de la chance, vous venez de remporter une clé, vous en avez désormer", str(cle) )
        continue


while cle != 3 and Dif == 2 :
    if cle == 3 :
        break 
    if cle < 0 :
        cle = 0
    Serpant = randint (1, 5)
    Serpant2 = randint (1, 5)

    Jarre = input("Choisissez quelle jarre vous voullez mettre la main (1 à 5) : ")

    if int(Jarre) == Serpant :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == Serpant2 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) > 5 :
        print ("Vous avez mis un nombre superieur a 5, recommencez")
    else :
        cle += 1
        print ("Piouff , vous avez de la chance, vous venez de remporter une clé, vous en avez désormer", str(cle) )
        continue


while cle != 3 and Dif == 3 :
    if cle == 3 :
        break 
    if cle < 0 :
        cle = 0
    
    serpant = randint (1, 10)
    serpant2 = randint (1, 10)
    serpant3 = randint (1, 10)
    serpant4 = randint (1, 10)
    serpant5 = randint (1, 10)
    serpant6 = randint (1, 10)

    Jarre = input("Choisissez quelle jarre vous voullez mettre la main (1 à 10) : ")
    
    if int(Jarre) == serpant :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == serpant2 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == serpant3 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == serpant4 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == serpant5 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) == serpant6 :
        print ("Aie ... vous vous etes fait mordre. ")
        cle -= 3
    elif int(Jarre) > 10 :
        print ("Vous avez mis un nombre superieur a 5, recommencez")
    else :
        cle += 1
        print ("Piouff , vous avez de la chance, vous venez de remporter une clé, vous en avez désormer", str(cle) )
        continue


print ("Bravo , vous etes devenu le maitre du temple")

a1 = input ()
