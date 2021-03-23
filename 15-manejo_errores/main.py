#Capturar excepciones y manejar errores en codigo
#suceptible a fallos/errores

try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, el nombre tienen que tener al menos un caracter")
else:
    print("Todo funciona correctamente")
finally:
    print("Fin de la iteración !!!!")




    



