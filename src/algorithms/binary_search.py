def minimum_essai(nb_min:int=1, nb_max:int=10000):
    from numpy import random

    nb_aleatoire = random.randint(nb_min, nb_max)
    essai = 0

    while True:
        nb_choisi = (nb_min + nb_max) // 2
        essai += 1
        if nb_choisi == nb_aleatoire:
            return essai
        elif nb_choisi < nb_aleatoire:
            nb_min = nb_choisi
        else:
            nb_max = nb_choisi