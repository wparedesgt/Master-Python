"""
La variable local se mantienen unicamente dentro de una funcion.

Las variables locales se encuentran dentro o fuera de una funcion.

"""

#Variable Global

frase = 'Ni los genios son tan genios, ni los mediocres estan mediocres'

print(frase)

def holaMundo():
    frase = 'Hola Mundo!!!'
    print('Dentro de la funcion')
    print(frase)
    global website
    website = 'datosgt.com'

holaMundo()

print(website)


