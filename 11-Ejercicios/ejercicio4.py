""""
Ejercicio No. 4.
- Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano 
y que imprima un mensaje segun el tipo de datos de cada variable.

"""

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = 'Lista'
    elif tipo == str:
        result = 'String'
    elif tipo == int:
        result = 'Entero'
    elif result == bool:
        result = 'Boleano'
    else:
        result = 'No coincide con ningun tipo '
    return result


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"Este dato es de tipo: {traducirTipo(tipo)}"
    else:
        result = 'Este dato no es correcto'
    
    return result

mi_lista = ["hola mundo", 77]
titulo = "Master en Python"
numero = 1000
verdadero = True


print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))

