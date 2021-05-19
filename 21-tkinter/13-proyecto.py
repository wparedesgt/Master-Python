"""
Crear una programa que contenga:

-ventana (hecho)
-tamaño fijo (hecho)
-ventana no redimensionable (hecho)
-Un Menu (Inicio, Añadir, Informacion, Salir) (hecho)
-Diferentes Pantallas
-Formulario de Añadir Productos
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
        padx=20,
        pady=20
    )
    home_label.grid(row=0,column=0)
    #Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0,column=0)
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0,column=0)
    data_label.grid(row=1,column=0)
    return True

#Definir Campos de Pantalla
home_label = Label(ventana, text="Inicio")
add_label = Label(ventana, text="Añadir Producto")
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