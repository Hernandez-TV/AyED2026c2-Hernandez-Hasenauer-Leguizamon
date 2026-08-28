import unittest
from ayedfiuner.estructuras.punto import Punto
from ayedfiuner.estructuras.poligono import Poligono


class TestPoligono(unittest.TestCase):

    def test_creacion_valida(self):
        p1 = Punto(0, 0)
        p2 = Punto(1, 0)
        p3 = Punto(0, 1)

        pol = Poligono([p1, p2, p3])

        self.assertEqual(len(pol.vertices), 3)

    def test_menos_de_tres_vertices(self):
        p1 = Punto(0, 0)
        p2 = Punto(1, 0)

        with self.assertRaises(ValueError):
            Poligono([p1, p2])

    def test_vertice_tipo_invalido(self):
        p1 = Punto(0, 0)
        p2 = Punto(1, 0)

        with self.assertRaises(TypeError):
            Poligono([p1, p2, "no es punto"])

    def test_perimetro_triangulo_rectangulo(self):
        # Triángulo 3-4-5
        p1 = Punto(0, 0)
        p2 = Punto(3, 0)
        p3 = Punto(3, 4)

        pol = Poligono([p1, p2, p3])

        # Lados: 3 + 4 + 5 = 12
        self.assertAlmostEqual(pol.obtener_perimetro(), 12.0)

    def test_vertices_copia_defensiva(self):
        p1 = Punto(0, 0)
        p2 = Punto(1, 0)
        p3 = Punto(0, 1)

        vertices = [p1, p2, p3]
        pol = Poligono(vertices)

        # Modifico la lista original
        vertices.append(Punto(2, 2))

        self.assertEqual(len(pol.vertices), 3)


if __name__ == "__main__":
    unittest.main()