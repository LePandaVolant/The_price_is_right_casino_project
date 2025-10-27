def strategie1(mise:int = 10, nb_essai:int = 100000) -> int: 
    mise_de_depart = mise
    benefices = 0

    from src.statistics.analysis import moy_minimum_essai

    list_essais = moy_minimum_essai(nb_essai=nb_essai)
    for essai in list_essais:
        if essai <= 6:
            benefices -= mise_de_depart * 10 - mise_de_depart
        elif essai <= 8:
            benefices -= mise_de_depart * 8 - mise_de_depart
        elif essai <= 9:
            benefices -= mise_de_depart * 5 - mise_de_depart
        elif essai <= 10:
            benefices -= mise_de_depart * 4 - mise_de_depart
        elif essai <= 11:
            benefices -= mise_de_depart * 2 - mise_de_depart
        else:
            benefices += mise_de_depart

    return benefices