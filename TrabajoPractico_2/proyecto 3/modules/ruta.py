class Ruta:
    """
    Representa una ruta de transporte.
    """

    def __init__(
        self,
        destino,
        capacidad,
        precio
    ):
        """
        PRE:
            capacidad > 0
            precio > 0

        POST:
            crea una ruta.
        """
        self.destino = destino
        self.capacidad = capacidad
        self.precio = precio

    def __str__(self):

        return (
            f"{self.destino}"
            f" ({self.capacidad} kg,"
            f" ${self.precio})"
        )