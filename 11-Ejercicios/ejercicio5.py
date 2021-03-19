"""
Ejercicio No.5

- Crear una lista con el contenido de esta tabla:

ACCION  AVENTURA           DEPORTES

GTA      ASSINS             FIFA 21
COD      CRASH              PRO 21
PUGB    PRINCE OR PERSIA    MOTO GP 21

Mostrar está información ordenada, accion, aventura y deportes

"""


tabla = [
    {
        "Categoria": "ACCION",
        "Juegos": [ "GTA", "Call of Dutty", "PUGB"]

    },
    {
        "Categoria": "AVENTURA",
        "Juegos": ["Assasins", "Crash Bandicoot", "Prince of persia"]
    },
    {
        "Categoria": "DEPORTES",
        "Juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"-----------{categoria['Categoria']} ----------")
    for juego in categoria['Juegos']:
        print(juego)


