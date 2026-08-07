import unittest
from ayedfiuner.algoritmos.burbuja import ordenamiento_burbuja

class TestOrdenamientoBurbuja(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(ordenamiento_burbuja([]), [])

    def test_lista_un_elemento(self):
        self.assertEqual(ordenamiento_burbuja([5]), [5])

    def test_lista_ordenada(self):
        self.assertEqual(ordenamiento_burbuja([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_lista_invertida(self):
        self.assertEqual(ordenamiento_burbuja([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_lista_mixta(self):
        self.assertEqual(ordenamiento_burbuja([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

    def test_lista_con_duplicados(self):
        self.assertEqual(ordenamiento_burbuja([3, 6, 8, 3, 2, 6, 1]), [1, 2, 3, 3, 6, 6, 8])
        
        
if __name__ == '__main__':
    unittest.main()