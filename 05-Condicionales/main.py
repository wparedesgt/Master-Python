"""
#Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de Comparacion 

== igual
!= diferente o distinto
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que


#Operadores Logicos

and Y
or  O
! negacion
not NO


"""

#Ejemplo 01

print("#################Ejemplo 01 ###############")

color = "rojo"

#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("En hora buena!!!")
    print("El color es ROJO")
else: 
    print("Color incorrecto")


#Ejemplo 02

print("\n #################Ejemplo 02 ###############")

year = 2020
#year = int(input("¿En que año estamos? "))

if year >= 2021:
    print("Estamos del 2021 en adelante !!!!")
else:
    print("Es un año anterior al 2021")


#Ejemplo 03

print("\n #################Ejemplo 03 ###############")

nombre = "William Paredes"
ciudad = "Guatemala"
continente = "Europa"
edad = 48
mayoria_edad = 18


if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "America":
        print("El usuario no es Americano")
    else:
        print(f"Es Americano y de {ciudad}")
else:
    print(f"{nombre} NO ES MAYOR DE EDAD")


#Ejemplo 04

print("\n #################Ejemplo 04 ###############")

dia = 2
#dia = int(input("Introduce el día de la semana: "))

"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es fin de semana")

"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es Fin de semana")


#Ejemplo 05

print("\n #################Ejemplo 05 ###############")

edad_minima = 18 
edad_maxima = 65
#edad_oficial = int(input("Introduce tu edad: "))

edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65 :
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

#Ejemplo 06

print("\n #################Ejemplo 06 ###############")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Guatemala":
    print(f"{pais}Es un pais de habla hispana")
else:
    print(f"{pais} No es un pais de habla hispana")


#Ejemplo 07

print("\n #################Ejemplo 07 ###############")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Guatemala"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")


#Ejemplo 08

print("\n #################Ejemplo 08 ###############")

pais = "Guatemala"

if pais != "Mexico" and pais != "España" and pais != "Guatemala":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")
