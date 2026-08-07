from ayedfiuner.estructuras.punto import Punto
from typing import List


class Poligono:
    """
    TAD Poligono: representa un polígono definido por una lista de puntos.
    
    Invariante:
        - Tiene al menos 3 puntos.
        - Todos los elementos son instancias de Punto.
    """

    def __init__(self, vertices: List[Punto]) -> None:
        if len(vertices) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")

        for v in vertices:
            if not isinstance(v, Punto):
                raise TypeError("Todos los vértices deben ser instancias de Punto.")

        self._vertices = vertices.copy()

    @property
    def vertices(self) -> List[Punto]:
        return self._vertices.copy()

    def obtener_perimetro(self) -> float:
        total = 0.0
        n = len(self._vertices)

        for i in range(n):
            current = self._vertices[i]
            punto_siguiente = self._vertices[(i + 1) % n]
            total += current.distancia_a(punto_siguiente)

        return total

    def __repr__(self) -> str:
        return f"Poligono({self._vertices})"