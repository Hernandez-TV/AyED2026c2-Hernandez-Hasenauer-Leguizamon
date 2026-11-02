from modules.grafo import Grafo

g = Grafo()

g.agregar_arista(
    "Buenos Aires",
    "Cordoba",
    500,
    20
)

print(
    g.vecinos(
        "Buenos Aires"
    )
)