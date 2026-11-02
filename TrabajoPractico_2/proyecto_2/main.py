from modules.temperaturas_db import Temperaturas_DB
db = Temperaturas_DB()

db.guardar_temperatura(
    25.6,
    "01/01/2024"
)

db.guardar_temperatura(
    30.1,
    "05/01/2024"
)

db.guardar_temperatura(
    18.4,
    "10/01/2024"
)

print(
    db.devolver_temperatura(
        "05/01/2024"
    )
)
