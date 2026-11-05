from datetime import datetime
from ayedfiuner.estructuras.arbol_avl import ArbolAVL


class Temperaturas_DB:
    """Base de datos de temperaturas implementada con AVL."""

    def __init__(self):
        """
        POST: crea una base de datos vacía.
        """
        self._avl = ArbolAVL()

    def _fecha(self, fecha):
        """
        PRE: fecha debe tener formato dd/mm/aaaa.
        POST: devuelve la fecha convertida a datetime.
        """
        return datetime.strptime(
            fecha,
            "%d/%m/%Y"
        )

    def guardar_temperatura(self, temperatura, fecha):
        """
        PRE: temperatura debe ser numérica.
        POST: almacena la temperatura asociada a la fecha.
        """
        self._avl.insertar(
            self._fecha(fecha),
            temperatura
        )

    def devolver_temperatura(self, fecha):
        """
        POST: devuelve la temperatura asociada a la fecha.
        """
        return self._avl.obtener(
            self._fecha(fecha)
        )

    def devolver_temperaturas(self, fecha1, fecha2):
        """
        POST: devuelve una lista con las temperaturas
        comprendidas en el rango.
        """
        inicio = self._fecha(fecha1)
        fin = self._fecha(fecha2)

        resultado = []

        def recorrer(nodo):

            if nodo is None:
                return

            if nodo.clave > inicio:
                recorrer(nodo.izquierdo)

            if inicio <= nodo.clave <= fin:

                resultado.append(
                    f"{nodo.clave.strftime('%d/%m/%Y')}: "
                    f"{nodo.valor} ºC"
                )

            if nodo.clave < fin:
                recorrer(nodo.derecho)

        recorrer(self._avl._raiz)

        return resultado

    def _obtener_valores_rango(
        self,
        fecha1,
        fecha2
    ):
        """
        POST: devuelve una lista con los valores
        de temperatura del rango.
        """
        inicio = self._fecha(fecha1)
        fin = self._fecha(fecha2)

        valores = []

        def recorrer(nodo):

            if nodo is None:
                return

            if nodo.clave > inicio:
                recorrer(nodo.izquierdo)

            if inicio <= nodo.clave <= fin:
                valores.append(nodo.valor)

            if nodo.clave < fin:
                recorrer(nodo.derecho)

        recorrer(self._avl._raiz)

        return valores

    def max_temp_rango(
        self,
        fecha1,
        fecha2
    ):
        """
        POST: devuelve la temperatura máxima
        del rango.
        """
        valores = self._obtener_valores_rango(
            fecha1,
            fecha2
        )

        return max(valores)

    def min_temp_rango(
        self,
        fecha1,
        fecha2
    ):
        """
        POST: devuelve la temperatura mínima
        del rango.
        """
        valores = self._obtener_valores_rango(
            fecha1,
            fecha2
        )

        return min(valores)

    def temp_extremos_rango(
        self,
        fecha1,
        fecha2
    ):
        """
        POST: devuelve (mínima, máxima)
        del rango.
        """
        valores = self._obtener_valores_rango(
            fecha1,
            fecha2
        )

        return (
            min(valores),
            max(valores)
        )

    def borrar_temperatura(
        self,
        fecha
    ):
        """
        POST: elimina la temperatura
        asociada a una fecha.
        """
        self._avl.eliminar(
            self._fecha(fecha)
        )

    def cantidad_muestras(self):
        """
        POST: devuelve la cantidad de
        temperaturas almacenadas.
        """
        return self._avl._tamanio