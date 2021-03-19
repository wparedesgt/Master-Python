"""
Ejercicio No. 3
- Programa que compruebe si una varible esta vacia y si esta vacia, rellenarla con texto
y mostrarlo en mayusculas

"""

texto = ''

if len(texto.strip()) <= 0:
    texto = 'hola soy un text en minusculas'
    print(texto.upper())
else:
    print(f'La variable tiene contenido: {texto}')    

