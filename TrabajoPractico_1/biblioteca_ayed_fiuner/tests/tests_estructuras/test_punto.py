import unittest
from ayedfiuner.estructuras.punto import Punto


class TestPunto(unittest.TestCase):

    def test_creacion_valida(self):
        p = Punto(1, 2)
        self.assertEqual(p.x, 1.0)
        self.assertEqual(p.y, 2.0)

    def test_creacion_tipo_invalido(self):
        with self.assertRaises(TypeError):
            Punto("a", 2)

        with self.assertRaises(TypeError):
            Punto(1, None)

    def test_distancia(self):
        p1 = Punto(0, 0)
        p2 = Punto(3, 4)
        self.assertAlmostEqual(p1.distancia_a(p2), 5.0)

    def test_distancia_tipo_invalido(self):
        p = Punto(0, 0)
        with self.assertRaises(TypeError):
            p.distancia_a("no es un punto")

    def test_repr(self):
        p = Punto(1, 2)
        self.assertEqual(repr(p), "Punto(1.0, 2.0)")


if __name__ == "__main__":
    unittest.main()