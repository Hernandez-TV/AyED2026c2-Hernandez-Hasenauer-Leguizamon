from modules.servicio_transporte import ServicioTransporte
from modules.lector_archivos import LectorArchivos


def main():
    """
    Programa principal del proyecto de transporte.
    """

    servicio = ServicioTransporte()

    LectorArchivos.cargar(
        "data/rutas.txt",
        servicio
    )

    origen = "CiudadBs.As."
    destino = "CiudadCordoba"
    peso = 50

    resultado = servicio.analizar_transporte(
        origen,
        destino,
        peso
    )

    print("RESULTADO DEL ANALISIS")
    print()

    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print()

    print(
        f"Máximo cuello de botella: "
        f"{resultado['peso_maximo']} kg"
    )

    print()

    print(
        f"Precio mínimo para transportar "
        f"{peso} kg: "
        f"{resultado['precio_minimo']}"
    )


if __name__ == "__main__":
    main()