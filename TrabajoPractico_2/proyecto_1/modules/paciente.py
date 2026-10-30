# -*- coding: utf-8 -*-

from random import randint, choices

nombres = [
    "Leandro",
    "Mariela",
    "Gastón",
    "Andrea",
    "Antonio",
    "Estela",
    "Jorge",
    "Agustina",
]

apellidos = [
    "Perez",
    "Colman",
    "Rodriguez",
    "Juarez",
    "García",
    "Belgrano",
    "Mendez",
    "Lopez",
]

niveles_de_riesgo = [1, 2, 3]

descripciones_de_riesgo = [
    "crítico",
    "moderado",
    "bajo",
]

# Probabilidades de aparición de cada tipo de paciente.
probabilidades = [0.1, 0.3, 0.6]


class Paciente:
    """Representa un paciente de la sala de emergencias."""

    def __init__(self):
        """
        POST: crea un paciente con nombre, apellido y nivel
        de riesgo generados aleatoriamente. El orden de
        llegada se inicializa en cero.
        """
        n = len(nombres)

        self.__nombre = nombres[randint(0, n - 1)]
        self.__apellido = apellidos[randint(0, n - 1)]

        self.__riesgo = choices(
            niveles_de_riesgo,
            probabilidades
        )[0]

        self.__descripcion = (
            descripciones_de_riesgo[self.__riesgo - 1]
        )

        self.__orden_llegada = 0

    def get_nombre(self):
        """
        POST: devuelve el nombre del paciente.
        """
        return self.__nombre

    def get_apellido(self):
        """
        POST: devuelve el apellido del paciente.
        """
        return self.__apellido

    def get_riesgo(self):
        """
        POST: devuelve el nivel de riesgo del paciente.
        """
        return self.__riesgo

    def get_descripcion_riesgo(self):
        """
        POST: devuelve la descripción del nivel de riesgo.
        """
        return self.__descripcion

    def set_orden_llegada(self, orden):
        """
        PRE: orden debe ser un entero positivo.
        POST: asigna el orden de llegada del paciente.
        """
        self.__orden_llegada = orden

    def get_orden_llegada(self):
        """
        POST: devuelve el orden de llegada del paciente.
        """
        return self.__orden_llegada

    def __lt__(self, otro):
        """
        PRE: otro debe ser un objeto Paciente.
        POST: devuelve True si este paciente tiene mayor
        prioridad que el otro.

        Se prioriza primero el riesgo y, en caso de empate,
        el orden de llegada.
        """
        return (
            self.__riesgo,
            self.__orden_llegada
        ) < (
            otro.__riesgo,
            otro.__orden_llegada
        )

    def __str__(self):
        """
        POST: devuelve una representación textual
        del paciente.
        """
        cad = self.__nombre + " "
        cad += self.__apellido + "\t -> "
        cad += str(self.__riesgo)
        cad += "-" + self.__descripcion

        return cad