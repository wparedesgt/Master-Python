from tkinter import *
from PIL import Image, ImageTk
import os



ventana = Tk()
ventana.geometry("700x500")
Label(ventana, text="Hola soy William").pack(anchor=W)
print(os.getcwd())
imagen = Image.open('21-tkinter/imagenes/lobo-gris-800.jpg')
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack()
ventana.mainloop()
