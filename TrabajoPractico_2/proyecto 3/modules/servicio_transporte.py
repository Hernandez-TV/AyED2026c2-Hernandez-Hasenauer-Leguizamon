from modules.grafo import Grafo
import heapq
class ServicioTransporte:
    """
    Gestiona las consultas del problema.
    """

    def __init__(self):

        self._grafo = Grafo()
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
    def precio_minimo(
        self,
        origen,
        destino,
        peso
    ):
        """
        POST:
            devuelve el precio mínimo
            transportable.
        """
        heap = [(0, origen)]

        costo = {
            origen: 0
        }

        while heap:

            costo_actual, ciudad = (
                heapq.heappop(heap)
            )

            if ciudad == destino:
                return costo_actual

            for (
                vecino,
                capacidad,
                precio
            ) in self._grafo.vecinos(ciudad):

                if capacidad < peso:
                    continue

                nuevo_costo = (
                    costo_actual +
                    precio
                )

                if (
                    vecino not in costo
                    or nuevo_costo
                    < costo[vecino]
                ):

                    costo[vecino] = (
                        nuevo_costo
                    )

                    heapq.heappush(
                        heap,
                        (
                            nuevo_costo,
                            vecino
                        )
                    )

        return None