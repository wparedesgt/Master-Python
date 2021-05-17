"""
CALCULADORA
    -Dos campos de texto
    -4 botones para las operaciones
    -Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox


ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

Numero1 = StringVar()
Numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=350, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5, 
    relief=SOLID, 
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(FALSE)


Label(marco, text="Primer Número: ").pack()
Entry(marco, textvariable=Numero1, justify=CENTER).pack()

Label(marco, text="Segundo Número: ").pack()
Entry(marco, textvariable=Numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar").pack(side="left", fill= X, expand=YES)
Button(marco, text="Restar").pack(side="left",fill= X, expand=YES)
Button(marco, text="Multiplicar").pack(side="left", fill= X, expand=YES)
Button(marco, text="Dividir").pack(side="left", fill= X, expand=YES)

ventana.mainloop()
