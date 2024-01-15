import unittest
from turing import decomposer_turing
from steve import decomposer_steve
class TestFunctions(unittest.TestCase):

    def test_decomposer_steve(self):
        # Tests unitaires pour decomposer() de steve
        assert decomposer_steve(123) == (1, 2, 3)
        assert decomposer_steve(999) == (9, 9, 9)
        pass
    
    def test_composer_turing(self):
        # Tests unitaires pour decomposer() de turing
        assert decomposer_turing(123) == (1, 2, 3)
        assert decomposer_turing(999) == (9, 9, 9)
        pass 

if __name__ == '__main__':
    unittest.main()