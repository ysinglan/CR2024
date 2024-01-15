import unittest
from turing import somme_turing
from steve import somme_steve
class TestFunctions(unittest.TestCase):

    def test_somme_steve(self):
        # Tests unitaires pour decomposer() de steve
        print(somme_steve(1, 2, 3))
        assert somme_steve(1, 2, 3) == True
        assert somme_steve(5, 5, 10) == True
        assert somme_steve(0, 0, 0) == True
        pass
    
    def test_somme_turing(self):
        # Tests unitaires pour decomposer() de turing
        print(somme_turing(1, 2, 3))
        assert somme_turing(1, 2, 3) == True
        assert somme_turing(5, 5, 10) == True
        assert somme_turing(0, 0, 0) == True
        pass 

if __name__ == '__main__':
    unittest.main()