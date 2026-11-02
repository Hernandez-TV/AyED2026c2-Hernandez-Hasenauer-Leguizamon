from modules.temperaturas_db import Temperaturas_DB


def main():

    print("=== TEST TEMPERATURAS DB ===\n")

    db = Temperaturas_DB()

    db.guardar_temperatura(
        25.5,
        "01/01/2024"
    )

    db.guardar_temperatura(
        30.2,
        "05/01/2024"
    )

    db.guardar_temperatura(
        18.7,
        "10/01/2024"
    )

    db.guardar_temperatura(
        22.4,
        "15/01/2024"
    )

    print("Temperatura del 05/01/2024:")

    print(
        db.devolver_temperatura(
            "05/01/2024"
        )
    )

    print()

    print("Máxima temperatura:")

    print(
        db.max_temp_rango(
            "01/01/2024",
            "15/01/2024"
        )
    )

    print()

    print("Mínima temperatura:")

    print(
        db.min_temp_rango(
            "01/01/2024",
            "15/01/2024"
        )
    )

    print()

    print("Temperaturas extrema:")

    print(
        db.temp_extremos_rango(
            "01/01/2024",
            "15/01/2024"
        )
    )

    print()

    print("Cantidad de muestras:")

    print(
        db.cantidad_muestras()
    )

    print()

    print("Listado:")

    temperaturas = (
        db.devolver_temperaturas(
            "01/01/2024",
            "15/01/2024"
        )
    )

    for t in temperaturas:
        print(t)

    print()

    print("Eliminando 10/01/2024")

    db.borrar_temperatura(
        "10/01/2024"
    )

    print()

    print("Nueva cantidad:")

    print(
        db.cantidad_muestras()
    )


if __name__ == "__main__":
    main()