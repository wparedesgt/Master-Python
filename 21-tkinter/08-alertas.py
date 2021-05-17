from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(
    bd=70
)

def sacarAlerta():
    MessageBox.showwarning("Alerta", "Hola este es un ejemplo de la alerta")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Continuar ejecutando la aplicacion?")
    if resultado != "yes":
        MessageBox.showinfo("Saludos", f"Buen Viaje: {nombre}")
        ventana.destroy()

Button(ventana, text="salir!!!", command=lambda: salir("William Paredes")).pack()


ventana.mainloop()
