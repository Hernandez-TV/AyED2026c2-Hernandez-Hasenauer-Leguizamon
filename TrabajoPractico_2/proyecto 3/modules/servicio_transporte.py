from modules.grafo import Grafo
class ServicioTransporte:
    """
    Gestiona las consultas del problema.
    """

    def __init__(self):

        self._grafo = Grafo()
    import heapq
    def maximo_cuello_botella(
        self,
        origen,
        destino
    ):
        """
        POST:
            devuelve la máxima capacidad
            transportable.
        """

        heap = [
            (-float("inf"), origen)
        ]

        mejor = {
            origen: float("inf")
        }

        while heap:

            capacidad_actual, ciudad = (
                heapq.heappop(heap)
            )

            capacidad_actual = (
                -capacidad_actual
            )

            if ciudad == destino:
                return capacidad_actual

            for (
                vecino,
                capacidad,
                _
            ) in self._grafo.vecinos(ciudad):

                nuevo = min(
                    capacidad_actual,
                    capacidad
                )

                if (
                    vecino not in mejor
                    or nuevo >
                    mejor[vecino]
                ):

                    mejor[vecino] = nuevo

                    heapq.heappush(
                        heap,
                        (
                            -nuevo,
                            vecino
                        )
                    )

        return 0