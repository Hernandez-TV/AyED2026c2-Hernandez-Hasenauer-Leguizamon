class LectorTemperaturas:
    """Carga temperaturas desde un archivo."""

    @staticmethod
    def cargar_archivo(ruta_archivo, bd):
        """
        PRE: ruta_archivo debe existir.

        POST: carga las temperaturas
        en la base de datos.
        """

        with open(
            ruta_archivo,
            encoding="utf-8"
        ) as archivo:

            for linea in archivo:

                fecha, temperatura = (
                    linea.strip()
                    .split(";")
                )

                bd.guardar_temperatura(
                    float(temperatura),
                    fecha
                )