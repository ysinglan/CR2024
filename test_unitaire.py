# test_functions.py
import unittest
from turing import decomposer, divisible, somme

class TestFunctions(unittest.TestCase):

    def test_decomposer(self):
        # Tests unitaires pour decomposer()
        assert decomposer(123) == (1, 2, 3)
        assert decomposer(999) == (9, 9, 9)

    def test_divisible(self):
        # Tests unitaires pour divisible()
        assert divisible(81) == True
        assert divisible(100) == False

def test_somme(self):
    # Tests unitaires pour somme()
    print(somme(1, 2, 3))
    assert somme(1, 2, 3) == True
    assert somme(5, 5, 10) == True
    assert somme(0, 0, 0) == True

if __name__ == '__main__':
    unittest.main()
