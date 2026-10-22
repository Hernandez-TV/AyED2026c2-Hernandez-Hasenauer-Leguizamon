from biblioteca_ayed_fiuner.ayedfiuner.algoritmos.RoundRobin  import round_robin
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
        ## Turnaround = Finalizacion - Llegada
        turnaround = (
            proceso.finalizacion
            - proceso.llegada
        )
        ## Waiting = Turnaround - Burst
        waiting = (
            turnaround
            - proceso.burst
        )

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
        turnaround = (
            proceso.finalizacion
            - proceso.llegada
        )
        waiting = (
            turnaround
            - proceso.burst
        )
        print(
            proceso.pid,
            proceso.llegada,
            proceso.burst,
            turnaround,
            waiting,
            sep="\t\t"
        )
    print("\n")

    