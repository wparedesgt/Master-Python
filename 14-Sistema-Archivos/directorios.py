import os
import pandas

# Crear carpeta

if not os.path.isdir("./14-Sistema-Archivos/mi_carpeta"):
    os.mkdir("./14-Sistema-Archivos/mi_carpeta")
else:
    print("Ya existe el directorio")


# Eliminar una carpeta

#os.rmdir("./14-Sistema-Archivos/mi_carpeta")

contenido = os.listdir("./14-Sistema-Archivos/mi_carpeta")

print("Contenido de mi carpeta: " + str(contenido))

for fichero in contenido:
    print("Fichero: " + fichero)

