
#Añadir métodos setters y getters. Opcional: Utilizar 
#propiedades (property) para ocultar setters y getters.
#Crear una unidad de prueba para validar tipo de datos
class Persona:
    def __init__(self,nombre:str,apellido:str):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    @property
    def nombre(self):
        return self.__nombre
    def set_nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido
    def set_apellido(self, value):
        self.__apellido = value

    @nombre.setter
    def nombre(self,value):
        if isinstance(value,str) and value[0].isupper():
            self.__nombre = value
        else:
            raise ValueError('El nombre debe ser un string, con la primera letra en mayuscula')
        
    @apellido.setter
    def apellido(self,value):
        if isinstance(value,str) and value[0].isupper():
            self.__apellido = value
        else:
            raise ValueError('El apellido debe ser un string, con la primera letra en mayuscula')

if __name__ == "__main__":
    p = Persona("Juan","Perez")
    print("Nombre:", p.nombre)
    print("Apellido:", p.apellido)

    # p1 = Persona("ana","Gomez")
    # print("Nombre:", p1.nombre)
    # print("Apellido:", p1.apellido)

    p2 = Persona(123,"Gomez")
    print("Nombre:", p2.nombre)