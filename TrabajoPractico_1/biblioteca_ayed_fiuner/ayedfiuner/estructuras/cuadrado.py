class cuadrado:
    def __init__(self, lado:float):
        if not isinstance(lado, (int,float)):
            raise TypeError("Lado debe ser un valor númerico")
        self.__lado = lado
    @property
    def lado(self) -> float:
        return self.__lado
    def get_lado(self):
        return self.__lado
    def area(self):
        return self.__lado ** 2

    def perimetro(self):
        return 4*self.__lado
    
    
if __name__ == "__main__":
    # Prueba local de un objeto de la clase Circulo
    c = cuadrado("h")
    print("Lado del cuadrado:", c.get_lado())
    print("Área del cuadrado:", c.area())
    print("Perímetro del cuadrado:", c.perimetro())