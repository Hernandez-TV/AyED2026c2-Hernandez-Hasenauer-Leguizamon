class Grafo:
    """
    Implementa un grafo dirigido.
    """

    def __init__(self):
        """
        POST:
            crea un grafo vacío.
        """
        self._vertices = {}
    def agregar_vertice(
        self,
        ciudad
    ):
        """
        POST:
            agrega la ciudad al grafo.
        """
        if ciudad not in self._vertices:
            self._vertices[ciudad] = []
    def agregar_arista(
        self,
        origen,
        destino,
        capacidad,
        precio
    ):
        """
        POST:
            agrega una ruta.
        """

        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        self._vertices[origen].append(
            (
                destino,
                capacidad,
                precio
            )
        )
    def vecinos(
        self,
        ciudad
    ):
        """
        POST:
            devuelve las rutas salientes.
        """

        return self._vertices.get(
            ciudad,
            []
        )
