from src.strategies.strategy1 import strategie1
from src.strategies.strategy2 import strategie2
from src.strategies.strategy3 import strategie
import pytest

def test_strategie1():
    assert strategie1(mise=10, nb_essai=100) is not None

def test_strategie2():
    assert strategie2(mise=10, nb_essai=100) is not None

def test_strategie3():
    assert strategie(mise=10, nb_essai=100) is not None