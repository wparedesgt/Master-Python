nombre = 'William'

#Funciones generales

print(type(nombre))

#Detectar el tipado

comprobar = isinstance(nombre, str)

if comprobar:
    print('Esa variable es un string')
else:
    print('No es una cadena')

#limpiar espacios de un string

frase = '      mi contenido      '

print(frase.strip())

# Eliminar variables

year = 2021
print(year)

del year

#print(year)

#Comprobar variable vacia

texto = '  ff  '

if len(texto) <= 0:
    print('La variable esta vacia')
else:
    print('La Variable tiene contenido: ', len(texto))


#Encontrar caracteres

frase = 'La vida es bella'

print(frase.find('vida'))

#Reemplazar palabras en un string

nueva_frase = frase.replace('vida', 'moto')

print(nueva_frase)

#Procesar Mayusculas y Minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())




