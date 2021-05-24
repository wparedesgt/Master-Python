"""
Crear una programa que contenga:

-ventana (hecho)
-tamaño fijo (hecho)
-ventana no redimensionable (hecho)
-Un Menu (Inicio, Añadir, Informacion, Salir) (hecho)
-Diferentes Pantallas (Hecho)
-Formulario de Añadir Productos (Hecho)
-Guardar datos temporalmente
-Listar datos en pantalla principal
-Opcion de Salir (Hecho)

"""
from tkinter import *

#Definir la ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Master en Python")
ventana.resizable(0,0)

#Pantallas

def home():
    #Montar Pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0,column=0)
    
    #Ocultar otras pantallas
    add_frame.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0,column=0, columnspan=10)
    #Campos del formulario
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_decription_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_decription_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12), 
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    #Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    info_label.grid(row=0,column=0)
    data_label.grid(row=1,column=0)
    #Ocultar otras pantallas
    add_frame.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()
    return True

#Variables Importantes

name_data = StringVar()
price_data = StringVar()


#Definir Campos de Pantalla (INICIO)
home_label = Label(ventana, text="Inicio")

#Definir Campos de Pantalla (Añadir Producto)
add_label = Label(ventana, text="Añadir Producto")

#Campos del formulario

add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label= Label(add_frame, text="Descripcion: ")
add_decription_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar")


#Definir Campos de Pantalla (Informacion)
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por William Paredes 2021")


#Cargar pantalla de inicio

home()

#Menu Superior

menu_superior = Menu(ventana)
menu_superior.add_command(label= "Inicio", command=home)
menu_superior.add_command(label= "Añadir", command=add)
menu_superior.add_command(label= "Informacion", command=info)
menu_superior.add_command(label= "Salir", command=ventana.quit)

#Cargar Menu
ventana.config(menu=menu_superior)

#Cargar la ventana
ventana.mainloop()