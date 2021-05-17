from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

#Texto Encabezado 
encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white", 
    bg="darkgray", 
    font=("Open Sans", 18), 
    padx=10,
    pady=10
)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
#encabezado.pack(side=LEFT, anchor=NW)
encabezado.grid(row=0, column=0, columnspan=3, sticky=W)

#Label para el campo (Nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

#Campo de texto

campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


#Label para el campo (Apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#Campo de texto

campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5)




ventana.mainloop()

