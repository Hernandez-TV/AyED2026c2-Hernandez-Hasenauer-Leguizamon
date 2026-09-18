

class cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.__lado

    @property
    def lado(self):
        return self.__lado
    def set_lado(self, value):
        if value < 0:
            raise ValueError("El lado del cuadrado no puede ser negativo.")
        self.__lado = value

    @lado.setter
    def lado(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__lado = value
        else:
            raise ValueError("El lado del cuadrado debe ser un numero natural positivo")

    def area(self):
        return self.lado ** 2


    def perimetro(self):
        return 4 * self.lado

if __name__ == "__main__":
    
    c = cuadrado(5)
    print("Lado del cuadrado:", c.lado)
    print("Área del cuadrado:", c.area())
    print("Perímetro del cuadrado:", c.perimetro())
    c1 = cuadrado(-10)
    print("Lado del cuadrado:", c1.lado)
    print("Área del cuadrado:", c1.area())
    print("Perímetro del cuadrado:", c1.perimetro())
    