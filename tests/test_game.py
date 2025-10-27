import unittest
from src.game.interactive_game import jouer_juste_prix

class TestInteractiveGame(unittest.TestCase):

    def test_jouer_juste_prix(self):
        # This test will need to be adapted for interactive input
        # You can use mocking to simulate user input for a more thorough test
        self.assertIsNone(jouer_juste_prix(20))  # Assuming the function returns None when quitting

if __name__ == '__main__':
    unittest.main()