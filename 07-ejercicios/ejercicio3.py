"""
Ejercicio 3.

Imprimir por pantalla los cuadrados de los 60 primeros numeros naturales

Bucle while y for

"""

contador = 1
resultado = 0

for contador in range(1,61):
    resultado = pow(contador,2)
    print(f"El cuadrado de: {contador} es: {resultado}")
    

print("#############################################")

contador = 1


while contador <=60:
    resultado = pow(contador, 2)
    print(f"El cuadrado de: {contador} es: {resultado}")
    contador += 1
