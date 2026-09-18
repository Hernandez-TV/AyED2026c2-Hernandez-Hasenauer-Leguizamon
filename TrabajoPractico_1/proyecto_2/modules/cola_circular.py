class ColaCircular: #se recomienda hacer con una cola doble enlazada, pero si pasa el test se puede dejar asi
    def __init__(self, capacidad):
        self.capacidad = capacidad #define tamanio de la cola
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def esta_llena(self):
        return self.tamanio == self.capacidad

    def encolar(self, elemento):
        if self.esta_llena():
            raise Exception("La cola circular está llena")
        self.cola[self.final] = elemento
        self.final = (self.final + 1) % self.capacidad
        self.tamanio += 1

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola circular está vacía")
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamanio -= 1
        return elemento

    def obtener_frente(self):
        if self.esta_vacia():
            raise Exception("La cola circular está vacía")
        return self.cola[self.frente]

    def obtener_tamanio(self):
        return self.tamanio

    def vaciar(self):
        self.cola = [None] * self.capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0

    def __init__(self, capacidad):
        if not isinstance(capacidad, int):
            raise TypeError("La capacidad debe ser un número entero")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo")
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamanio = 0
        