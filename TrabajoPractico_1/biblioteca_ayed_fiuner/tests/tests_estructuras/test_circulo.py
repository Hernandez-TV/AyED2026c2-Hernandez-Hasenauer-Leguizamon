import unittest
from ayedfiuner.estructuras.circulo import Circulo

class TestCiculo(unittest.TestCase):
    def test_area(self):
        c = Circulo(5)
        self.assertAlmostEqual(c.area(), 78.53981633974483)

    def test_perimetro(self):
        c = Circulo(5)
        self.assertAlmostEqual(c.perimetro(), 31.41592653589793)
        

if __name__ == '__main__':
    unittest.main()