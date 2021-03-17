"""
FUNCIONES: 

Una funcion es un conjunto de instrucciones agrupadas en un nombre concreto que puede 
reutilizarse invocando la funcion tantas veces como sea necesario.

def nombreDeMiFuncion(parametros o argumentos):
    #Bloque de codigo o conjunto de intrucciones

NombreDeMiFuncion(parametros o argumentos)

"""

#Ejemplo 01
print('#####EJEMPLO 1 #######')

def muestraNombre():
    print('Will')
    print('Paco')
    print('Tono')
    print('Chepe')
    print('Viny')
    print('Nicho')
    print('\n')


#Invocar a la funcion

muestraNombre()

# Ejemplo No2: Parametros
print('#####EJEMPLO 2 #######')

def mostrarTuNombre(Su_Nombre, edad):
    print(f"Tu nombre es: {Su_Nombre}")
    if edad >= 18:
        print('Y eres mayor de edad!!!')


#nombre = input("Introduce tu nombre: ")
#edad = int(input("Introduce tu edad: "))

#mostrarTuNombre(nombre, edad)

# Ejemplo No3: Parametros
print('#####EJEMPLO 3 #######')

def tabla(numero):
    print(f"Tabla de multiplicar del número {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f'{numero} X {contador} = {operacion}')
    
    print('\n')

tabla(3)
tabla(7)
tabla(12)

#Ejemplo 3.1

for ntabla in range(1,11):
    tabla(ntabla)



# Ejemplo No4: Parametros
print('#####EJEMPLO 4 #######')

# Parametros opcionales

def getEmpleado(nombre, cui = None):
    print('EMPLEADO')
    print(f'Nombre: {nombre}')

    if cui != None:
        print(f'CUI:  {cui}')
    

getEmpleado('William', 158653073)

# Ejemplo No5: Parametros
print('#####EJEMPLO 5 #######')

#Devolver datos de una funcion

def saludame(nombre):
    saludo = f'Hola Saludos {nombre} '
    return saludo

print(saludame("William"))

#Ejemplo No. 6 Calculadora en un string

print('\n #####EJEMPLO 6 #######')

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1/numero2

    cadena = ''

    if basicas != False:

        cadena += 'Suma: ' + str(suma) 
        cadena += '\n'
        cadena += 'Resta' + str(resta)
        cadena += '\n'
    else:
    
        cadena += 'Multiplicacion' + str(multi)
        cadena += '\n'
        cadena += 'Division' + str(division)

    return(cadena)

print(calculadora(5,5))



#Ejemplo No. 7 Funciones dentro de funciones

print('\n #####EJEMPLO 7 #######')

def getNombre(Nombre):
    texto = f'El nombre es: {Nombre}'
    return texto

def getApellidos(Apellidos):
    texto = f'Los apellidos son: {Apellidos}'
    return texto


print(getNombre("William"), getApellidos("Paredes"))


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + '\n' + getApellidos(apellidos)
    return texto

print(devuelveTodo('William', 'Paredes'))


#Ejemplo No. 8 Funcion lambda (funciones anonimas)

print('\n #####EJEMPLO 8 #######')
dime_el_year = lambda year: f'El año es {year + 50}'

print(dime_el_year(2034))













