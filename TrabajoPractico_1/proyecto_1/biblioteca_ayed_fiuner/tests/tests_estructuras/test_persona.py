import unittest

from ayedfiuner.estructuras.Persona import Persona


class TestPersona(unittest.TestCase):
    def test_creacion_valida(self):
        persona = Persona("Ana", "García")
        self.assertEqual(persona.nombre, "Ana")
        self.assertEqual(persona.apellido, "García")
        self.assertEqual(persona.nombre_completo(), "Ana García")

    def test_tipo_de_dato_invalido(self):
        with self.assertRaises(TypeError):
            Persona(123, "García")

        with self.assertRaises(TypeError):
            Persona("Ana", 456)

    def test_campo_debe_estar_capitalizado(self):
        with self.assertRaises(ValueError):
            Persona("ana", "García")

        with self.assertRaises(ValueError):
            Persona("Ana", "garcía")


if __name__ == "__main__":
    unittest.main()
