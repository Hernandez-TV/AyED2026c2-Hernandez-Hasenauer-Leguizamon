import random
import time
from ayedfiuner.algoritmos.bubble_sort import bubble_sort
from ayedfiuner.algoritmos.quick_sort import quick_sort
from ayedfiuner.algoritmos.radix_sort import radix_sort
def medir_algoritmos():
    tamanios = []
    tiempos_burbuja = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = []
    for n in range(500, 5001, 500):
        lista = [
            random.randint(10000, 99999)
            for _ in range(n)
        ]
        tamanios.append(n)
        # Bubble Sort
        copia = lista.copy()
        inicio = time.perf_counter()
        bubble_sort(copia)
        fin = time.perf_counter()
        tiempos_burbuja.append(fin - inicio)
        # Quick Sort
        copia = lista.copy()
        inicio = time.perf_counter()
        quick_sort(copia)
        fin = time.perf_counter()
        tiempos_quick.append(fin - inicio)
        # Radix Sort
        copia = lista.copy()
        inicio = time.perf_counter()
        radix_sort(copia)
        fin = time.perf_counter()
        tiempos_radix.append(fin - inicio)
        # Sorted de Python
        copia = lista.copy()
        inicio = time.perf_counter()
        sorted(copia)
        fin = time.perf_counter()
        tiempos_sorted.append(fin - inicio)
    return (
        tamanios,
        tiempos_burbuja,
        tiempos_quick,
        tiempos_radix,
        tiempos_sorted
    )