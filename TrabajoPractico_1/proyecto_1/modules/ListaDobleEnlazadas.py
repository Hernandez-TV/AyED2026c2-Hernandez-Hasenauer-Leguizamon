class Nodo:
    def __init__(self,datoinicial):
        self.dato = datoinicial
        self.siguiente = None
        self.anterior = None

@property
def dato(self):
    return self._dato

@property
def siguiente(self):
    return self._siguiente

@siguiente.setter
def siguiente(self, nuevo_siguiente):
        #Establece la referencia al siguiente nodo.
        #Precondición: nuevo_siguiente debe ser una instancia de la clase Nodo o None.
        #Postcondición: _siguiente se actualiza con nuevo_siguiente.
        
        if nuevo_siguiente is not None and not isinstance(nuevo_siguiente, Nodo):
            raise TypeError("El siguiente elemento debe ser una instancia de Nodo o None")
        self._siguiente = nuevo_siguiente

@property
def anterior(self,nuevo_anterior):
    
        #Establece la referencia al nodo anterior.
        #Precondición: nuevo_anterior debe ser una instancia de la clase Nodo o None.
        #Postcondición: _anterior se actualiza con nuevo_anterior.
        
        if nuevo_anterior is not None and not isinstance(nuevo_anterior, Nodo):
            raise TypeError("El elemento anterior debe ser una instancia de Nodo o None")
        self._anterior = nuevo_anterior

@anterior.setter
def anterior(self, nuevo_anterior):
    self._anterior = nuevo_anterior

class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza= None
        self._cola = None
        self._tamanio = 0
    @property
    def cabeza(self):
        return self._cabeza
    
    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self._tamanio += 1

    def agregar_al_final(self,item):
        """si la lista está vacía, el item que se agrega es cabeza y cola"""
        temp = Nodo(item)
        if self.esta_vacia() :
            self.cabeza = self.cola = temp
        else: #Si no está vacía, el nodo pasa a ser 'cola' siendo 'anterior' el enlace con referencia del nodo que estaba al cola de la lista
            self.cola.siguiente = temp #El puntero 'siguiente' del 'cola anterior' apunta al 'nuevo cola' que es temp 
            temp.anterior = self.cola #El puntero 'anterior' de temp señala la 'cola anterior'
            self.cola = temp #temp pasa a ser el nuevo 'cola'
        self._tamanio += 1

    def insertar(self, item, posicion = None):
        if posicion is None or posicion == self._tamanio:
            self.agregar_al_inicio(item)
        elif posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion < 0 or posicion> self._tamanio:
            raise IndexError("Posición fuera de rango.")
        else:
            nuevo = Nodo(item)
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            anterior.siguiente = nuevo
            actual.anterior = nuevo
            self._tamanio += 1
    
    def extraer(self, posicion = None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        
        if posicion is None or posicion == -1:
            #Elimina el último
            nodo_extraido = self.cola
            if self.cabeza == self.cola:
                self.cabeza = self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        elif posicion == 0:
            nodo_extraido = self.cabeza
            if self.cabeza == self.cola:
                self.cabeza = self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
        elif posicion < 0 or posicion >= self._tamanio:
            raise IndexError("posición fuera de rango.")
        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            else:
                self.cola = actual.anterior
            nodo_extraido = actual

        self._tamanio -= 1
        return nodo_extraido.dato
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia
    
    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente,actual.anterior
            actual = actual.anterior # porque ahora los enlaces están invertidos
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self,otralista):
        actual= otralista.cabeza
        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual= actual.siguiente
        return self
    
    def __len__(self):
            return self._tamanio

    def __add__(self,otralista):
        temp = self.copiar()
        return temp.concatenar(otralista.copiar())

    def __iter__(self):
        actual=self.cabeza
        while actual is not None:
            yield actual.dato
            actual=actual.siguiente

    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)