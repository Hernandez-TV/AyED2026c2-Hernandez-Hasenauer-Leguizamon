from ayedfiuner.estructuras.grafo import Grafo
from ayedfiuner.estructuras.ColaDePrioridad import ColaPrioridad


class ServicioTransporte:
    """
    Gestiona las consultas del problema de transporte.
    """

    def __init__(self):
        """
        POST: crea un servicio de transporte vacío.
        """
        self._grafo = Grafo()

    def agregar_ruta(
        self,
        origen,
        destino,
        capacidad,
        precio
    ):
        """
        POST: agrega una ruta al grafo.
        """
        self._grafo.agregar_arista(
            origen,
            destino,
            capacidad,
            precio
        )

    def obtener_peso_maximo(
        self,
        origen,
        destino
    ):
        """
        POST: devuelve el máximo cuello de botella
        entre origen y destino.
        """

        cola = ColaPrioridad()

        cola.encolar(
            (
                -float("inf"),
                origen
            )
        )

        mejor = {
            origen: float("inf")
        }

        while not cola.esta_vacia():

            capacidad_actual, ciudad = (
                cola.desencolar()
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
                    or nuevo > mejor[vecino]
                ):

                    mejor[vecino] = nuevo

                    cola.encolar(
                        (
                            -nuevo,
                            vecino
                        )
                    )

        return 0

    def obtener_precio_minimo(
        self,
        origen,
        destino,
        peso
    ):
        """
        POST: devuelve el costo mínimo para
        transportar un peso determinado.
        """

        cola = ColaPrioridad()

        cola.encolar(
            (
                0,
                origen
            )
        )

        costos = {
            origen: 0
        }

        while not cola.esta_vacia():

            costo_actual, ciudad = (
                cola.desencolar()
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
                    vecino not in costos
                    or nuevo_costo <
                    costos[vecino]
                ):

                    costos[vecino] = (
                        nuevo_costo
                    )

                    cola.encolar(
                        (
                            nuevo_costo,
                            vecino
                        )
                    )

        return None

    def analizar_transporte(
        self,
        origen,
        destino,
        peso
    ):
        """
        POST: coordina el cálculo del máximo
        cuello de botella y del costo mínimo
        para transportar el peso indicado.
        """

        peso_maximo = self.obtener_peso_maximo(
            origen,
            destino
        )

        precio_minimo = self.obtener_precio_minimo(
            origen,
            destino,
            peso
        )

        return {
            "peso_maximo": peso_maximo,
            "precio_minimo": precio_minimo,
        }
    def analizar_transporte(
        self,
        origen,
        destino,
        peso
    ):
        """
        POST: coordina el cálculo del máximo
        cuello de botella y del costo mínimo
        para transportar el peso indicado.
        """

        peso_maximo = self.obtener_peso_maximo(
            origen,
            destino
        )

        precio_minimo = self.obtener_precio_minimo(
            origen,
            destino,
            peso
        )

        return {
            "peso_maximo": peso_maximo,
            "precio_minimo": precio_minimo
        }