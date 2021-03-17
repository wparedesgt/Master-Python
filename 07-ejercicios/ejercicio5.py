"""

Ejercicio 5.

Programa que muestre todos los numeros entre dos numeros que diga el usuario

"""

#Entrada

Primer_Numero = int(input("Ingrese el primer numero: "))
Segundo_Numero = int(input("Ingrese el Segundo numero: "))

#Salida



##Otra respuesta

if Primer_Numero < Segundo_Numero:
    total = range((Primer_Numero +1 ), Segundo_Numero)
    print(f"Los numeros de enmedio son: {list(total)}")
    
else:
    print("El número 1 debe de ser menor al numero 2")

