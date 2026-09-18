from modules.cola_circular import ColaCircular

class Proceso:

    def __init__(self, pid, llegada, burst):
        self.pid = pid
        self.llegada = llegada
        self.burst = burst

        # Al principio falta ejecutar todo el burst
        self.restante = burst

        # Aquí se registra el tiempo en el que finalizó
        self.finalizacion = 0

def round_robin(procesos, quantum, tamanio_cola):

    cola = ColaCircular(tamanio_cola)

    tiempo = 0
    indice = 1

    # El primer proceso llega en t = 0
    cola.encolar(procesos[0])

    while (not cola.esta_vacia()) or indice < len(procesos):

        # Si la cola quedó vacía, adelantamos el reloj al próximo proceso
        if cola.esta_vacia():
            tiempo = procesos[indice].llegada
            cola.encolar(procesos[indice])
            indice += 1

        """
        PASO 1: Obtener el proceso a ejecutar
        Instrucción: Saca el primer proceso que esté esperando en la cola circular 
        para asignarle la CPU.
        """
        
        # TODO: Desencolar el proceso
        proceso = cola.desencolar() # Reemplazar esta línea


        """
        PASO 2: Determinar el tiempo de ejecución real
        Instrucción: El proceso ejecutará un máximo igual al 'quantum'. 
        Sin embargo, como se vio en el ejemplo del TP con el proceso P2 (que duraba 3 
        y el quantum era 4), si al proceso le falta menos tiempo que el quantum, 
        liberará la CPU anticipadamente. 
        Calcula cuánto tiempo exacto va a ejecutar en este ciclo.
        """
        """Comentario a grupo:condicion si es menor al quantum, se ejecuta el tiempo restante
        si es mayor o igual al quantum, se ejecuta el quantum"""
        if proceso.restante < quantum: 
            ejecucion = proceso.restante 
        else: 
            ejecucion = quantum
        # TODO: Calcular la variable 'ejecucion'
        #ejecucion = 0 # Reemplazar esta línea

        """
        PASO 3: Simular la ejecución en la CPU
        Instrucción: Actualiza el tiempo 'restante' del proceso restándole el 
        tiempo de ejecución calculado en el paso anterior. Luego, actualiza 
        la variable global 'tiempo' sumándole ese mismo valor.
        """
        # TODO: Actualizar 'proceso.restante' y 'tiempo'
        proceso.restante -= ejecucion
        tiempo += ejecucion


        """
        PASO 4: Encolar procesos recién llegados ("Preemption")
        Instrucción: Como se detalla en el TP (cuando llegan P2 y P3 en medio de la 
        ejecución de P1), ANTES de volver a encolar el proceso actual, debes 
        verificar si llegaron nuevos procesos al sistema durante el tiempo que 
        acaba de transcurrir, y agregarlos a la cola.
        Ayuda: Usa un ciclo while comprobando si 'indice' es menor a la cantidad total 
        de procesos y si el tiempo de 'llegada' de ese proceso es menor o igual al 'tiempo' actual.
        """
        # TODO: Encolar los procesos que hayan llegado mientras la CPU estaba ocupada
        while indice < len(procesos) and procesos[indice].llegada <= tiempo:
            cola.encolar(procesos[indice])
            indice += 1

        """
        PASO 5: Verificación de finalización o reencolado
        Instrucción: Verifica si el proceso actual terminó su ejecución (tiempo restante es 0).
        - Si terminó: Guarda el 'tiempo' actual en la variable 'finalizacion' del proceso.
        - Si NO terminó: El proceso es "preempted" y debe volver al final de la cola circular 
          para continuar más adelante.
        """
        # TODO: Comprobar estado final del proceso y actuar en consecuencia
        

if __name__ == "__main__":

    # Caso de prueba 1 (Ejemplo explicado en el TP)
    procesos_1 = [
        Proceso("P1", 0, 6),
        Proceso("P2", 3, 3),
        Proceso("P3", 6, 7)
    ]

    print("--- CASO DE PRUEBA 1 (Quantum = 4) ---")
    round_robin(procesos_1, 4, 10)
    print("ProcessID\tArrivalTime\tBurstTime\tTurnaround Time\tWaitingTime")

    for proceso in procesos_1:
        """
        PASO 6: Cálculos finales
        Instrucción: Siguiendo las fórmulas del TP, calcula el 'turnaround' y el 'waiting' time.
        - Turnaround = tiempo de finalización - tiempo de llegada.
        - Waiting = Turnaround - duración (burst time).
        """
        # TODO: Calcular 'turnaround' y 'waiting'
        turnaround = 0 # Reemplazar esta línea
        waiting = 0 # Reemplazar esta línea

        print(
            proceso.pid,
            proceso.llegada,
            proceso.burst,
            turnaround,
            waiting,
            sep="\t\t"
        )
    
    # Caso de prueba 2 (Requerido en el TP)
    procesos_2 = [
        Proceso("P1", 0, 5),
        Proceso("P2", 2, 3),
        Proceso("P3", 3, 1),
        Proceso("P4", 5, 2),
        Proceso("P5", 6, 5),
        Proceso("P6", 8, 4)
    ]

    print("--- CASO DE PRUEBA 2 (Quantum = 2) ---")
    round_robin(procesos_2, 2, 10)
    print("ProcessID\tArrivalTime\tBurstTime\tTurnaround Time\tWaitingTime")

    for proceso in procesos_2:
        # TODO: Aplicar los mismos cálculos de turnaround y waiting
        turnaround = 0 # Reemplazar esta línea
        waiting = 0 # Reemplazar esta línea

        print(
            proceso.pid,
            proceso.llegada,
            proceso.burst,
            turnaround,
            waiting,
            sep="\t\t"
        )
    print("\n")

    