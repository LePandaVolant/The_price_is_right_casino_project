import unittest
from src.algorithms.binary_search import minimum_essai

class TestAlgorithms(unittest.TestCase):

    def test_minimum_essai(self):
        # Test with default parameters
        result = minimum_essai()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)

        # Test with a smaller range
        result = minimum_essai(1, 10)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

        # Test with a larger range
        result = minimum_essai(1, 100000)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)

if __name__ == '__main__':
    unittest.main()