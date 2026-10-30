from modules.ColaDePrioridad import ColaPrioridad
class SalaEmergencias:
    """Administra el ingreso y la atención de pacientes."""

    def __init__(self):
        """
        POST: crea una sala de emergencias vacía con una
        cola de prioridad para gestionar pacientes.
        """
        self._cola = ColaPrioridad()
        self._orden_llegada = 0

    def ingresar_paciente(self, paciente, riesgo):
        """
        PRE: paciente debe ser una instancia de Paciente.
        POST: agrega el paciente a la cola de prioridad
        asignándole un orden de llegada.
        """
        self._orden_llegada += 1

        paciente.set_orden_llegada(
            self._orden_llegada
        )

        self._cola.encolar(paciente)

    def atender_paciente(self):
        """
        PRE: debe existir al menos un paciente en espera.
        POST: elimina y devuelve el paciente con mayor
        prioridad de atención.
        """
        return self._cola.desencolar()

    def esta_vacia(self):
        """
        POST: devuelve True si no hay pacientes esperando
        ser atendidos; devuelve False en caso contrario.
        """
        return self._cola.esta_vacia()

    def cantidad_pacientes(self):
        """
        POST: devuelve la cantidad de pacientes actualmente
        en espera.
        """
        return len(self._cola)

    def __str__(self):
        """
        POST: devuelve una representación de los pacientes
        en espera.
        """
        return str(self._cola)