class Punto:
    """
    TAD Punto: representa un punto en el plano 2D.
    Invariante:
        - x e y son números (int o float)
    """

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x e y deben ser valores numéricos.")
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def distancia_a(self, other: "Punto") -> float:
        if not isinstance(other, Punto):
            raise TypeError("El argumento debe ser un Punto.")
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Punto({self._x}, {self._y})"