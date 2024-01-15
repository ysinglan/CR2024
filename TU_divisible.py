import unittest
from turing import divisible_turing
from steve import divisible_steve
class TestFunctions(unittest.TestCase):

    def test_divisible_steve(self):
        # Tests unitaires pour divisible() de steve
        assert divisible_steve(81) == True
        assert divisible_steve(100) == False
        pass
    
    def test_divisible_turing(self):
        # Tests unitaires pour divisible() de turing
        assert divisible_turing(81) == True
        assert divisible_turing(100) == False
        pass 

if __name__ == '__main__':
    unittest.main()