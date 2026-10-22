from ayedfiuner.estructuras.cola_circular import ColaCircular

def round_robin(procesos, quantum, tamanio_cola):
    
    """ Simula la planificación de CPU mediante el algoritmo Round Robin. 
    Precondición:
        - 'procesos' es una lista de objetos Proceso ordenados por tiempo de llegada. 
        - 'quantum' es un entero positivo (>0). 
        - 'tamanio_cola' es la capacidad máxima de la ColaCircular. 
    Postcondición: 
        - Retorna la lista de procesos con sus tiempos de finalización, 
        retorno y espera calculados. """
    
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
        proceso = cola.desencolar() 
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

        """
        PASO 3: Simular la ejecución en la CPU
        Instrucción: Actualiza el tiempo 'restante' del proceso restándole el 
        tiempo de ejecución calculado en el paso anterior. Luego, actualiza 
        la variable global 'tiempo' sumándole ese mismo valor.
        """
        #Actualizamos el tiempo restante del proceso y el reloj global del sistema 
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
        # Si el proceso terminó, guardamos el instante en el que finalizó su ejecución
        if proceso.restante == 0:
            proceso.finalizacion = tiempo
        #Si todavía le queda tiempo de CPU, vuelve al final de la cola (Round Robin)
        else:
            cola.encolar(proceso)
    return procesos
