def esperance(mise:int=10, nb_essai:int=1000000, strat=None):
    if strat is None:
        from src.strategies.strategy1 import strategie1 as strat
    m = mise
    n = nb_essai
    esperance = strat(m, n) / n

    return esperance