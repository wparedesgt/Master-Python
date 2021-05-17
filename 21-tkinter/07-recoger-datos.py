from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50
)

def get_dato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto:").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido").pack(anchor=NW)
text_recogido = Label(ventana, textvariable=resultado)
text_recogido.config(
    bg="green", 
    fg="white"
)
text_recogido.pack(anchor=NW)



Button(ventana, text="Mostrar Dato", command=get_dato).pack(anchor=NW)


ventana.mainloop()
