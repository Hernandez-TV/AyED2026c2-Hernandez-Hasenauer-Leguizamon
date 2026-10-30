class MonticuloBinario:
    """Representa un montículo binario de mínimos."""

    def __init__(self):
        """
        POST: crea un montículo binario vacío.
        """
        self._elementos = [None]
        self._tamanio = 0

    def esta_vacio(self):
        """
        POST: devuelve True si el montículo está vacío;
        devuelve False en caso contrario.
        """
        return self._tamanio == 0

    def __len__(self):
        """
        POST: devuelve la cantidad de elementos almacenados
        en el montículo.
        """
        return self._tamanio

    def insertar(self, elemento):
        """
        PRE: elemento debe ser comparable con los elementos
        almacenados en el montículo.
        POST: agrega elemento al montículo respetando la
        propiedad de orden.
        """
        self._elementos.append(elemento)
        self._tamanio += 1
        self._flotar(self._tamanio)

    def eliminar_minimo(self):
        """
        PRE: el montículo no debe estar vacío.
        POST: elimina y devuelve el elemento mínimo del
        montículo.
        """
        minimo = self._elementos[1]

        self._elementos[1] = self._elementos[self._tamanio]
        self._elementos.pop()

        self._tamanio -= 1

        if self._tamanio > 0:
            self._hundir(1)

        return minimo

    def ver_minimo(self):
        """
        PRE: el montículo no debe estar vacío.
        POST: devuelve el elemento mínimo sin eliminarlo.
        """
        return self._elementos[1]

    def _flotar(self, posicion):
        """
        PRE: posicion corresponde a un índice válido del
        montículo.
        POST: reubica el elemento en su posición correcta
        hacia arriba para mantener la propiedad de orden.
        """
        while posicion // 2 > 0:

            padre = posicion // 2

            if self._elementos[posicion] < self._elementos[padre]:

                self._elementos[posicion], self._elementos[padre] = (
                    self._elementos[padre],
                    self._elementos[posicion]
                )

            posicion = padre

    def _hundir(self, posicion):
        """
        PRE: posicion corresponde a un índice válido del
        montículo.
        POST: reubica el elemento en su posición correcta
        hacia abajo para mantener la propiedad de orden.
        """
        while posicion * 2 <= self._tamanio:

            hijo_minimo = self._obtener_hijo_minimo(posicion)

            if self._elementos[posicion] > self._elementos[hijo_minimo]:

                self._elementos[posicion], self._elementos[hijo_minimo] = (
                    self._elementos[hijo_minimo],
                    self._elementos[posicion]
                )

            posicion = hijo_minimo

    def _obtener_hijo_minimo(self, posicion):
        """
        PRE: posicion corresponde a un nodo que posee al menos
        un hijo.
        POST: devuelve la posición del hijo con menor valor.
        """
        if posicion * 2 + 1 > self._tamanio:
            return posicion * 2

        if self._elementos[posicion * 2] < self._elementos[posicion * 2 + 1]:
            return posicion * 2

        return posicion * 2 + 1