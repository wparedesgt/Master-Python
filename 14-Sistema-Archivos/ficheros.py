from io import open
import pathlib
import shutil

#Abrir un archivo
#archivo = open("14-Sistema-Archivos/fichero_texto.txt", "a+")
ruta = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_texto.txt"
#print(ruta)

archivo = open(ruta, "a+")

# Escribir

archivo.write("************texto ingresado desde python**************************\n")

# Cerrar archivo

archivo.close


#Abrir Archivo

ruta = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()
#Print contenido


#Leer contenido y guardarlo en lista

lista = archivo_lectura.readlines()
archivo_lectura.close

for frase in lista:
    lista_frase = frase.split()
    #if not frase.isnumeric():
    print("- " + frase.capitalize())
    #print(lista_frase)

#Copiar, renombrar y eliminar un archivo

#copiar

#ruta_original = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_texto.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_copiado.txt"
#ruta_alternativa = str(pathlib.Path().absolute()) + "#j3mplo de cualquier ruta"
#shutil.copyfile(ruta_original, ruta_nueva)

#mover 

#ruta_original = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_copiado.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_copiado_NUEVO.txt"

#shutil.move(ruta_original, ruta_nueva)

#Eliminar
import os

#ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_copiado_NUEVO.txt"
#os.remove(ruta_nueva)

#comprobar si el archivo exite

import os.path

#print(os.path.abspath("./"))

#print(os.path.isfile(os.path.abspath("./") + "/14-Sistema-Archivos/fichero_copiado_NUEVO.txt"))

if os.path.isfile(os.path.abspath("./") + "/14-Sistema-Archivos/fichero_copiado_NUEVO.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")








os.remove





