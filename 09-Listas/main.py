"""
Colecciones de datos bajo un unico nombre.

Para acceder a esos valores podemos usar un indice númericos.

"""

pelicula = 'Batman'

print(pelicula)

#Definir una lista

peliculas = ['Batman', 'Spiderman', 'El Señor de los Anillos'] #Tuplas
cantantes = list(('Arjona', 'Jeniffer Lopez', 'Madona')) #Metodos
years = list(range(2020,2050))
variada = ['William', '120909', True, 'Texto']

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:1])
print(cantantes[0:2])
print(cantantes[1:])

peliculas[1] = "Gran Torino"

print(peliculas)

#Agregar Elementos a una lista

cantantes.append('Brian Jhonson')
cantantes.append('Facundo Cabral')

print(cantantes)

#Recorrer y mostrar una lista utilizando el bucle for

print('\n######LISTADO DE PELICULAS#########')

"""

nueva_pelicula = ''

while nueva_pelicula != 'parar':
    nueva_pelicula = input('Introduce la nueva pelicula: ')
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)



for pelicula in peliculas:
    print(f'{peliculas.index(pelicula)+1}. {pelicula}')

"""

# Listas multidimensionales

print('\n ########Listado de Contactos')

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

print(contactos[1][1])

for contacto in contactos:
    print('\n')
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print('Nombre: ' + elemento)
        else:
            print('Email: ' + elemento)


        







