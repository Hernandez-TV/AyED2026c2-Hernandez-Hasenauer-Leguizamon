class NodoAVL:
    """Representa un nodo de un árbol AVL."""

    def __init__(self, clave, valor):
        """
        PRE: clave debe ser comparable.

        POST: crea un nodo AVL.
        """
        self.clave = clave
        self.valor = valor

        self.izquierdo = None
        self.derecho = None

        self.altura = 1