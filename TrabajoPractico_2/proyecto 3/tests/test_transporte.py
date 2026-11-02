from modules.servicio_transporte import (
    ServicioTransporte
)

s = ServicioTransporte()

s._grafo.agregar_arista(
    "Buenos Aires",
    "Cordoba",
    500,
    20
)

s._grafo.agregar_arista(
    "Cordoba",
    "Mendoza",
    300,
    15
)

print(
    s.maximo_cuello_botella(
        "Buenos Aires",
        "Mendoza"
    )
)

print(
    s.precio_minimo(
        "Buenos Aires",
        "Mendoza",
        250
    )
)