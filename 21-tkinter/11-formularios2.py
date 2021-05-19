from tkinter import *

ventana = Tk()

ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)

#encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)

encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

#Botones check

def MostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo Web "


    if movil.get():
        texto += "Analista de Datos"


    
    mostrar.config(
        text=texto, 
        bg="green", 
        fg="white"
        )

web = IntVar()
movil = IntVar()


Label(ventana, text="A que te dedicas").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo Web",
    variable=web,
    onvalue=1, 
    offvalue=0,
    command=MostrarProfesion    
    ).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="Analista Datos",
    variable=movil, 
    onvalue=1,
    offvalue=0,
    command=MostrarProfesion
    ).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row= 4, column=0)

#Radio Buttons
def marcar():
    marcado.config(text= opcion.get())



opcion = StringVar()
opcion.set(None)

Label(ventana, text="Cual es tu genero").grid(row=5, column=0)
Radiobutton(
    ventana, 
    text="Masculino", 
    value="Masculino",
    variable=opcion, 
    command=marcar
    ).grid(row=6, column=0)
Radiobutton(
    ventana, 
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
    ).grid(row=7, column=0)

marcado = Label(ventana)
marcado.grid(row=8, column=0)

#Option Menu
def seleccionar():
    seleccionado.config(text= opcion.get())

opcion = StringVar()
opcion.set("Opcion1")

Label(ventana, text="Selecciona una opcion").grid(row=5, column=1)

Select = OptionMenu(ventana,opcion, "Opcion1", "Opcion2", "Opcion3" )
Select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()
