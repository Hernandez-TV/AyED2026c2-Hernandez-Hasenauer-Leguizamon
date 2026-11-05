from modules.lector_temperaturas import (
    LectorTemperaturas
)

from modules.temperaturas_db import Temperaturas_DB
db = Temperaturas_DB()

LectorTemperaturas.cargar_archivo(
    "data/muestras.txt",
    db
)

print(
    db.cantidad_muestras()
)
