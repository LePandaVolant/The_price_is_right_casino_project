def strategie(mise:int =10,nb_essai:int =100000): 
    mise_de_depart = mise

    benefices = 0

    list_essais = moy_minimum_essai(nb_essai=nb_essai)
    for essai in list_essais:
        if essai <= 4:
            benefices -= mise_de_depart*15 - mise_de_depart
        elif essai <= 9 :
            benefices -= mise_de_depart*8 - mise_de_depart
        elif essai <= 10:
            benefices -= mise_de_depart*4 - mise_de_depart
        elif essai <= 11:
            benefices -= mise_de_depart*2 - mise_de_depart
        else:
            benefices += mise_de_depart

    return benefices