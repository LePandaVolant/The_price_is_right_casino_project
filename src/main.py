def main():
    from algorithms.binary_search import minimum_essai
    from statistics.analysis import moy_minimum_essai
    from strategies.strategy1 import strategie1
    from strategies.strategy2 import strategie2
    from strategies.strategy3 import strategie
    from game.interactive_game import jouer_juste_prix

    # Example of running the simulation
    print("Running gambling simulation...")
    print(f"Average attempts to guess the number: {round(average(moy_minimum_essai()), 0)}")
    
    # Run interactive game
    jouer_juste_prix()

if __name__ == "__main__":
    main()