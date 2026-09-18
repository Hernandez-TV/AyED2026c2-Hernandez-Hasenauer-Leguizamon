from ayedfiuner.algoritmos.burbuja import ordenamiento_burbuja
from ayedfiuner.estructuras.circulo import Circulo
from ayedfiuner.estructuras.punto import Punto
from ayedfiuner.estructuras.poligono import Poligono


# Ejemplo de uso del algoritmo de ordenamiento burbuja
lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = ordenamiento_burbuja(lista)
print("Lista ordenada:", lista_ordenada)


# Ejemplo de uso de la estructura Circulo
circulo1 = Circulo(1)
circulo5 = Circulo(5)

print("Radio del círculo de radio 1:", circulo1.get_radio())
print("Radio del círculo de radio 5:", circulo5.get_radio())

print("Área del círculo de radio 1:", circulo1.area())
print("Área del círculo de radio 5:", circulo5.area())

# Ejemplo de uso de Polígono (un TAD que dentro utiliza otro TAD)
p1 = Punto(1, 1)
p2 = Punto(2, 0)
p3 = Punto(1, 2)

un_poligono = Poligono([p1, p2, p3])

print(un_poligono)