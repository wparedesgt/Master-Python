"""
Ejercicio 9.
Programa que nos pida un numero los va mostrando en pantalla hasta que el usuario ingrese 111
"""

contador = 1

while contador < 100:
    numero = int(input("Introduce un numero: "))
    if numero == 111:
        break
    else:
        print(f"Has introducido el: {numero}")


