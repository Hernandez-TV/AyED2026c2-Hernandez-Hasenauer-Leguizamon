class LectorArchivos:
    """
    Carga rutas desde archivo.
    """
    @staticmethod
    def cargar(
        archivo,
        servicio
    ):
        """
        POST:
            carga las rutas desde el archivo al servicio
            de transporte.
        """
        with open(
            archivo,
            encoding="utf-8"
        ) as f:

            for linea in f:

                origen, destino, capacidad, precio = (
                    linea.strip().split(",")
                )

                servicio._grafo.agregar_arista(
                    origen,
                    destino,
                    int(capacidad),
                    int(precio)
                )
