#import os

#print(os.getcwd())

#tkinter es un modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

# Crear una ventana raiz

ventana = Tk()

#Titulo de la ventana

ventana.title("Interfas grafica con Python")

#Comprobar si existe un archivo

ruta_icono = os.path.abspath('/home/wparedes/Documentos/Documentos01/CienciaDatos/Master-Python/Master-Python/21-tkinter/imagenes/logotipo.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/logotipo.ico')


#Icono de la ventana

#ventana.iconbitmap(ruta_icono)

#Mostrar texto en el programa

texto = Label(ventana, text = ruta_icono)

texto.pack()



# Cambio en el tamaño de la ventna

ventana.geometry("750x450")

#Bloquear el tamaño de la ventana

ventana.resizable(0,0)


# Arrancar y mostrar la ventana hasta que se cierre

ventana.mainloop()

