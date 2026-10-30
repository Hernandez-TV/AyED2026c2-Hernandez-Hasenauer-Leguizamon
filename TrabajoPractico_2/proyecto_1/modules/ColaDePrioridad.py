from modules.MonticuloBinario import MonticuloBinario
class ColaPrioridad:
    """Implementa una cola de prioridad mediante un montículo."""

    def __init__(self):
        """
        POST: crea una cola de prioridad vacía.
        """
        self._monticulo = MonticuloBinario()

    def esta_vacia(self):
        """
        POST: devuelve True si la cola está vacía;
        False en caso contrario.
        """
        return self._monticulo.esta_vacio()

    def encolar(self, elemento):
        """
        PRE: elemento debe ser comparable con los demás
        elementos almacenados.
        POST: agrega elemento a la cola respetando
        las prioridades.
        """
        self._monticulo.insertar(elemento)

    def desencolar(self):
        """
        PRE: la cola no debe estar vacía.
        POST: elimina y devuelve el elemento de mayor
        prioridad.
        """
        return self._monticulo.eliminar_minimo()

    def frente(self):
        """
        PRE: la cola no debe estar vacía.
        POST: devuelve el elemento de mayor prioridad
        sin eliminarlo.
        """
        return self._monticulo.ver_minimo()

    def __len__(self):
        """
        POST: devuelve la cantidad de elementos almacenados
        en la cola.
        """
        return len(self._monticulo)