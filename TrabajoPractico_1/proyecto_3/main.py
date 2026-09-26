#Para probar cada modulo 
from modules.bubble_sort import bubble_sort
datos = [8, 3, 5, 1, 9]
print("Lista original:")
print(datos)
ordenada = bubble_sort(datos.copy())
print("Lista ordenada:")
print(ordenada) 

from modules.quick_sort import quick_sort
datos = [8, 3, 5, 1, 9]
print("QuickSort")
print("Original:")
print(datos)
print("Ordenada:")
print(quick_sort(datos)) 

from modules.radix_sort import radix_sort
datos = [329, 457, 657, 839, 436, 720, 355]
print("Radix Sort")
print("Original:")
print(datos)
print("Ordenada:")
print(radix_sort(datos))

import matplotlib.pyplot as plt
from modules.benchmark import medir_algoritmos
(
tamanios,
tiempos_burbuja,
tiempos_quick,
tiempos_radix,
tiempos_sorted
) = medir_algoritmos()

plt.plot(
tamanios,
tiempos_burbuja,
label="Bubble Sort"
)

plt.plot(
tamanios,
tiempos_quick,
label="QuickSort"
)

plt.plot(
tamanios,
tiempos_radix,
label="Radix Sort"
)

plt.plot(
tamanios,
tiempos_sorted,
label="sorted()"
)
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparacion de algoritmos")
plt.legend()
plt.grid()
plt.show()