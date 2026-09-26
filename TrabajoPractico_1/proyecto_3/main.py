#Para probar cada modulo 
"""from modules.bubble_sort import bubble_sort
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
print(quick_sort(datos)) """

from modules.radix_sort import radix_sort
datos = [329, 457, 657, 839, 436, 720, 355]
print("Radix Sort")
print("Original:")
print(datos)
print("Ordenada:")
print(radix_sort(datos))