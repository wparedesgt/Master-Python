#tkinter es un modulo para crear interfaces graficas de usuario

from tkinter import *

# Crear una ventana raiz

ventana = Tk()

# Cambio en el tamaño de la ventna

ventana.geometry("750x450")

#Bloquear el tamaño de la ventana

ventana.resizable(0,0)


# Arrancar y mostrar la ventana hasta que se cierre

ventana.mainloop()

