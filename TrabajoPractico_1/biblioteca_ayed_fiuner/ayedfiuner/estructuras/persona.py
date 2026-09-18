class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:    
        self.set_nombre = nombre
        self.set_apellido = apellido

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @nombre.setter
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, (str)):
            raise TypeError("El nombre debe ser de tipo string")
        if not nombre.istitle():
            raise ValueError("El nombre debe estar capitalizado")
        self.__nombre = str(nombre)
    
    @apellido.setter
    def set_apellido(self, apellido: str) -> None:
            if not isinstance(apellido, (str)):
                raise TypeError("El apellido debe ser de tipo string")
            if not apellido.istitle():
                raise ValueError("El apellido debe estar capitalizado")
            self.__apellido = str(apellido)
   

if __name__ == "__main__":
    p=Persona(1, "Pérez")
    print("Nombre:", p.nombre)
    print("Apellido:", p.apellido)
    # Prueba local de un objeto de la clase Persona
    # try:
    #     n =  "juan"
    #     p = Persona(n, "Pérez")
    # except ValueError as e:
    #     m="Juan"
    #     p = Persona(n, "Pérez")
    #     print("Error:", e)
    #print("Nombre:", p.nombre)
    
    #print("Apellido:", p.apellido)
