# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""
import datetime
import random
import time

import modules.paciente as pac
from modules.SalaDeEmergencia import SalaEmergencias

def main():
    n = 20  # cantidad de ciclos de simulación

    sala = SalaEmergencias()

    # Ciclo que gestiona la simulación
    for i in range(n):

        # Fecha y hora de entrada de un paciente
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime("%d/%m/%Y %H:%M:%S")

        print("-*-" * 15)
        print("\n", fecha_y_hora, "\n")

        # Se crea un paciente por segundo
        paciente = pac.Paciente()

        # Se ingresa a la sala de emergencias
        sala.ingresar_paciente(paciente,paciente.get_riesgo())

        print("Ingresa:", paciente)

        # Atención de paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5 and not sala.esta_vacia():

            paciente_atendido = sala.atender_paciente()

            print("*" * 40)
            print("Se atiende el paciente:", paciente_atendido)
            print("*" * 40)

        print()
        print("Pacientes que faltan atenderse:")

        # Mostrar pacientes en espera
        print(sala)

        print()
        print("-*-" * 15)

        time.sleep(1)

if __name__ == "__main__":
    main()
