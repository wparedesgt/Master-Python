"""
Ejercicio1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:

- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por el teclado)

"""

lista1 = list(range(1,9))
numeros = [15,24,19,28,20,33,16,25]

print(numeros)
print(numeros.sort)
print(len(numeros))

for numero in numeros:
    print(numero)


def mostrarLista(lista):
    resultado = ''

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += '\n'
        return resultado


print(mostrarLista(numeros))

print(mostrarLista(['Victor', 'Juan', 'Pepe']))

numeros.sort()
print(mostrarLista(numeros))


#Busqueda en la lista

print('##########Busqueda en la lista ###############3')

busqueda = int(input('Introduce el número: '))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    Busqueda = int(input('Introduce el número: '))
else:
    print(f'Has introducido el {busqueda}')

print(f'#### Buscar en la lista el número {busqueda}')

search = numeros.index(busqueda)
print(f'El número buscado existe en la lista, el el indice:  {search}')


