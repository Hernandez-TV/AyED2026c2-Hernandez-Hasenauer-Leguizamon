from modules.nodo_avl import NodoAVL


class ArbolAVL:
    """Implementación de Árbol AVL."""

    def __init__(self):
        """
        POST: crea un árbol AVL vacío.
        """
        self._raiz = None
        self._tamanio = 0

    #altura de un nodo
    def _altura(self, nodo):
        """
        POST: devuelve la altura de un nodo.
        """
        if nodo is None:
            return 0

        return nodo.altura
        
    #factor de balance
    def _factor_balance(self, nodo):
        """
        POST: devuelve el factor de balance.
        """
        if nodo is None:
            return 0

        return (
            self._altura(nodo.izquierdo)
            - self._altura(nodo.derecho)
        )
    
    #rotación a la derecha
    def _rotar_derecha(self, y):

        x = y.izquierdo
        t2 = x.derecho

        x.derecho = y
        y.izquierdo = t2

        y.altura = 1 + max(
            self._altura(y.izquierdo),
            self._altura(y.derecho)
        )

        x.altura = 1 + max(
            self._altura(x.izquierdo),
            self._altura(x.derecho)
        )

        return x
    
    #rotación a la izquierda
    def _rotar_izquierda(self, x):

        y = x.derecho
        t2 = y.izquierdo

        y.izquierdo = x
        x.derecho = t2

        x.altura = 1 + max(
            self._altura(x.izquierdo),
            self._altura(x.derecho)
        )

        y.altura = 1 + max(
            self._altura(y.izquierdo),
            self._altura(y.derecho)
        )

        return y
    
    def insertar(self, clave, valor):
        """
        PRE: clave debe ser comparable.

        POST: inserta el elemento manteniendo
        el balance del AVL.
        """
        self._raiz = self._insertar(
            self._raiz,
            clave,
            valor
        )

    def _insertar(
        self,
        nodo,
        clave,
        valor
    ):
        """
        POST: inserta el elemento manteniendo el balance del AVL.
        """

        if nodo is None:
            self._tamanio += 1
            return NodoAVL(
                clave,
                valor
            )

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar(
                nodo.izquierdo,
                clave,
                valor
            )

        elif clave > nodo.clave:
            nodo.derecho = self._insertar(
                nodo.derecho,
                clave,
                valor
            )

        else:
            nodo.valor = valor
            return nodo

        nodo.altura = 1 + max(
            self._altura(nodo.izquierdo),
            self._altura(nodo.derecho)
        )

        balance = self._factor_balance(
            nodo
        )

        # Izquierda-Izquierda

        if (
            balance > 1
            and clave < nodo.izquierdo.clave
        ):
            return self._rotar_derecha(nodo)

        # Derecha-Derecha

        if (
            balance < -1
            and clave > nodo.derecho.clave
        ):
            return self._rotar_izquierda(nodo)

        # Izquierda-Derecha

        if (
            balance > 1
            and clave > nodo.izquierdo.clave
        ):
            nodo.izquierdo = self._rotar_izquierda(
                nodo.izquierdo
            )

            return self._rotar_derecha(nodo)

        # Derecha-Izquierda

        if (
            balance < -1
            and clave < nodo.derecho.clave
        ):
            nodo.derecho = self._rotar_derecha(
                nodo.derecho
            )

            return self._rotar_izquierda(nodo)

        return nodo

    def obtener(self, clave):
        """
        PRE: clave debe existir.

        POST: devuelve el valor asociado.
        """

        actual = self._raiz

        while actual:

            if clave == actual.clave:
                return actual.valor

            if clave < actual.clave:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        raise KeyError(
            "La clave no existe."
        )
    def eliminar(self, clave):
        """
        PRE: clave debe existir.
        POST: elimina la clave del AVL.
        """
        self._raiz = self._eliminar(
            self._raiz,
            clave
        )
    def _minimo(self, nodo):
        """
        POST: devuelve el nodo mínimo
        del subárbol.
        """
        actual = nodo

        while actual.izquierdo:
            actual = actual.izquierdo

        return actual
    def _eliminar(
        self,
        nodo,
        clave
    ):

        if nodo is None:
            return nodo

        if clave < nodo.clave:

            nodo.izquierdo = self._eliminar(
                nodo.izquierdo,
                clave
            )

        elif clave > nodo.clave:

            nodo.derecho = self._eliminar(
                nodo.derecho,
                clave
            )

        else:
            if nodo.izquierdo is None:
                self._tamanio -= 1
                return nodo.derecho

            if nodo.derecho is None:
                self._tamanio -= 1
                return nodo.izquierdo

            temporal = self._minimo(
                nodo.derecho
            )

            nodo.clave = temporal.clave
            nodo.valor = temporal.valor

            nodo.derecho = self._eliminar(
                nodo.derecho,
                temporal.clave
            )

        if nodo is None:
            return nodo

        nodo.altura = 1 + max(
            self._altura(nodo.izquierdo),
            self._altura(nodo.derecho)
        )

        balance = self._factor_balance(
            nodo
        )

        if (
            balance > 1
            and self._factor_balance(
                nodo.izquierdo
            ) >= 0
        ):
            return self._rotar_derecha(
                nodo
            )

        if (
            balance > 1
            and self._factor_balance(
                nodo.izquierdo
            ) < 0
        ):

            nodo.izquierdo = (
                self._rotar_izquierda(
                    nodo.izquierdo
                )
            )

            return self._rotar_derecha(
                nodo
            )

        if (
            balance < -1
            and self._factor_balance(
                nodo.derecho
            ) <= 0
        ):
            return self._rotar_izquierda(
                nodo
            )

        if (
            balance < -1
            and self._factor_balance(
                nodo.derecho
            ) > 0
        ):

            nodo.derecho = (
                self._rotar_derecha(
                    nodo.derecho
                )
            )

            return self._rotar_izquierda(
                nodo
            )

        return nodo
