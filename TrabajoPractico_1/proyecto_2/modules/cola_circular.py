class ColaCircular: 
    def __init__(self, capacidad): 
        """se recomienda hacer con una cola doble enlazada, pero si pasa el test se puede dejar asi. 
En este caso se hace con una lista y se controla el frente y final de la cola, 
y el tamaño de la misma."""
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo")
        self.capacidad = capacidad #define tamanio de la cola
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0

    def esta_vacia(self):
        """
        PRE:
        Ninguna.
        POST:
        Devuelve True si la cola está vacía y False en caso 
        contrario.
        """
        return self.tamanio == 0

    def esta_llena(self):
        """
        PRE:
        Ninguna.
        POST:
        Devuelve True si la cola alcanzó su capacidad máxima y 
        False en caso contrario.
        """
        return self.tamanio == self.capacidad

    def encolar(self, elemento):
        """
        PRE:
        La cola no debe estar llena.
        POST:
        El elemento queda agregado al final de la cola y el 
        tamaño aumenta en una unidad.
        """
        if self.esta_llena():
            raise Exception("La cola circular está llena")
        self.cola[self.final] = elemento
        self.final = (self.final + 1) % self.capacidad
        self.tamanio += 1

    def desencolar(self):
        """
        PRE:
        La cola no debe estar vacía.
        POST:
        Se elimina y devuelve el elemento ubicado al frente de 
        la cola.
        El tamaño disminuye en una unidad.
        """
        if self.esta_vacia():
            raise Exception("La cola circular está vacía")
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamanio -= 1
        return elemento

    def obtener_frente(self):
        """
        PRE:
        La cola no debe estar vacía.
        POST:
        Devuelve el elemento ubicado al frente
        sin eliminarlo de la cola.
        """
        if self.esta_vacia():
            raise Exception("La cola circular está vacía")
        return self.cola[self.frente]

    def obtener_tamanio(self):
        """
        PRE:
            Ninguna.

        POST:
            Devuelve la cantidad actual de elementos
            almacenados en la cola.
        """
        return self.tamanio

    def vaciar(self):
        """
        PRE:
        Ninguna.
        POST:
        La cola queda vacía y todos los índices vuelven a su estado inicial.
        """
        self.cola = [None] * self.capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0

    def __init__(self, capacidad):
        """
        PRE:
            capacidad debe ser un número entero positivo.

        POST:
            Se crea una cola circular vacía con la capacidad
            indicada.
            frente y final se inicializan en 0.
            tamaño se inicializa en 0.

        EXCEPCIONES:
            TypeError si capacidad no es un entero.
            ValueError si capacidad es menor o igual a cero.
        """
        if not isinstance(capacidad, int):
            raise TypeError("La capacidad debe ser un número entero")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo")
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0
        