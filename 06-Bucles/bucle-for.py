"""
# FOR

for variable in elemento iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES


"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el " + str(contador))
    resultado = resultado + contador

print(f"El Resultado es : {resultado}")


#Ejemplo con tablas de multiplicar

print("\n############EJEMPLO##############")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1
print(f"\n#### Tabla de multimplicar del número {numero_usuario} #######")

for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("\n No se pueden mostrar numeros prohibidos")
        break
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla Finalizada")