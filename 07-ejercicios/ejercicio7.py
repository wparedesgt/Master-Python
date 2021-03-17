"""
Ejercicio 7.

Hacer un programa que muestre todos los numero impares entre dos numeros que decida el usuario

"""

Primer_Numero = int(input("Ingrese Primer Número: "))
Segundo_Numero = int(input("Ingrese Segundo Número: "))

if Primer_Numero <= Segundo_Numero:
    lista_numeros = range((Primer_Numero+1), Segundo_Numero )

for impar in lista_numeros:
    if impar%2 != 0:
        print(f"El numero es: {impar}")
else:
    print("El primer numero debe de ser menor que el segundo")


