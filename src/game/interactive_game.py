def jouer_juste_prix(argent_de_depart:int=20):
    from numpy import random
    benefices = 0
    argent = argent_de_depart
    while True:
        print("===============")
        print("Le Juste Prix")
        print("---------------")
        print("1) Jouer")
        print("2) Quitter")
        print("===============")
        reponse = int(input())
        if reponse != 1:
            return False
        else:
            if argent <=0:
                print("Vous n'avez plus assez d'argent pour continuer")
                return False
            print(f"Vous avez {argent} €")
            print("Combien voulez-vous miser ?")
            mise = int(input("Votre mise"))
            print(f"Vous avez misé {mise} €")

            nb_aleatoire = random.randint(1,10000)
            essai = 0
            trouve = False

            print("Le nombre a deviné a été choisi, c'est a vous :")
            while not trouve:
                nb_choisi = int(input("Choisissez un nombre"))
                essai += 1
                if nb_choisi == nb_aleatoire:
                    print("Vous avez trouvé")
                    trouve = True
                elif nb_choisi < nb_aleatoire:
                    print(f"Plus que {nb_choisi}")
                else:
                    print(f"Moins que {nb_choisi}")
            if essai <= 4:
                benefices -= mise*15 - mise
                argent += mise*15 - mise
                print("Vous avez réussi en 4 essais ou moins")
                print("Vous avez gagné 15 fois votre mise")
            elif essai <= 9 :
                benefices -= mise*8 - mise
                argent += mise*8 - mise
                print("Vous avez réussi en 9 essais ou moins")
                print("Vous avez gagné 8 fois votre mise")
            elif essai <= 10:
                benefices -= mise*5 - mise
                argent += mise*5 - mise
                print("Vous avez réussi en 10 essais")
                print("Vous avez gagné 5 fois votre mise")

            elif essai <= 11:
                benefices -= mise*2 - mise
                argent += mise*2 - mise
                print("Vous avez réussi en 11 essais")
                print("Vous avez gagné 2 fois votre mise")
            else:
                benefices += mise
                argent -= mise
                print("Vous avez réussi en plus de 11 essais")
                print("Vous avez perdu votre mise")
            print(f"Votre argent : {argent} €")