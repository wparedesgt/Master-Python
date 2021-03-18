"""
Es una lista que almacena un conjunto de valores con indices alfanumerico (array asociativo)
En formato clave > valor.
"""

persona = {
    'nombre': 'William', 
    'apellidos': 'Paredes',
    'web': 'www.datosgt.com'
}

print(persona)
print(type(persona))
print(persona['apellidos'])

#Lista con diccionarios

contactos = [
    {
        'nombre': 'William', 
        'email': 'wparedes@datosgt.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

contactos[0]['nombre'] = 'Vinicio'
print(contactos)
print(contactos[0]['nombre'])

print('\n Listado de Contactos: ')

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------------------------")





