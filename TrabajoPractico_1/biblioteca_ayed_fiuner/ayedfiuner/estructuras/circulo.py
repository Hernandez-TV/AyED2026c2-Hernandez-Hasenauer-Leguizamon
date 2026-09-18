from math import pi

class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def area(self):
        return pi * (self.__radio ** 2)

    def perimetro(self):
        return 2 * pi * self.__radio
    
    
if __name__ == "__main__":
    # Prueba local de un objeto de la clase Circulo
    c = Circulo(5)
    print("Radio del círculo:", c.get_radio())
    print("Área del círculo:", c.area())
    print("Perímetro del círculo:", c.perimetro())