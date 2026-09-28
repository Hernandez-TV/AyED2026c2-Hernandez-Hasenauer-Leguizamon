import matplotlib.pyplot as plt 
from random import randint
import time

from ListaDobleEnlazada import ListaDobleEnlazada


tamanos= [x for x in range(1,1001,100) ]

tiempos_len = []
tiempos_invertir = []
tiempos_copiar = []

for n in tamanos:
    lista = ListaDobleEnlazada()
   

    for _ in range(n):
        dato = randint(1, 100)
        lista.agregar_al_inicio(dato)
        
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        len(lista)
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempos_len.append(contador)

    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lista.copiar()
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempos_copiar.append(contador)
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempos_invertir.append(contador)
    
# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_invertir, marker='o', label="invertir - O(n)")
plt.plot(tamanos, tiempos_copiar, marker='o', label="copiar O(n)")
plt.plot(tamanos, tiempos_len, marker='o', label="len O(1)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo ejecución (segundos)')
plt.title('Comparación de tiempos de operaciones en Lista Doblemente Enlazada')
plt.legend()
plt.grid()
plt.show()