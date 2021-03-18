"""
Un set e un tipo de datos para tener una colección de valores sin indice ni orden
"""

personas = {
    'William',
    'Manolo',
    'Francisco'
}

print(personas)
print(type(personas))
personas.add('Paco')
print(personas)
personas.remove('Francisco')
print(personas)

