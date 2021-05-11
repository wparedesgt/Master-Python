from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 30)
)
texto.pack()

texto = Label(ventana, text="Soy William Paredes")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(anchor=E)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text=pruebas(pais="Guatemala",nombre="William", apellidos="Paredes")) #Se puede cambiar el orden al especificar el argumento
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(anchor=NW)


ventana.mainloop()




