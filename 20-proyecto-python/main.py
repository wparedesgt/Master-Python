"""
Proyecto Python y MySql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará 
- Crear nota, mostrar notas, borrarlas.
"""

print("""
Acciones disponibles:
    - registro 
    - login
""")

accion = input("Que quieres hacer?: ")

if accion == "registro":
    print("\n Ok!! Vamos a registrarte en el sistema...")
    nombre = input("Cual es tu Nombre?: ")
    apellidos = input("Cuales son tus apellidos?: ")
    email = input("Introduce tu emaiil: ")
    password = input("Introduce tu contraseña: ")

elif accion == "login":
    print("\n Identificate en el sistema...")    
    email = input("Introduce tu emaiil: ")
    password = input("Introduce tu contraseña: ")

import mysql.connector

#Conectar a base de datos

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "W1ll1@m2021",
    database = "master_python" 
)

