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

def CFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Inroduce Números")
    return result


def sumar():
        resultado.set(CFloat(Numero1.get()) + CFloat(Numero2.get()))
        mostrarresultado()
    

def restar():
        resultado.set(CFloat(Numero1.get()) - CFloat(Numero2.get()))
        mostrarresultado()
    
def multiplicar():
        resultado.set(CFloat(Numero1.get()) * CFloat(Numero2.get()))
        mostrarresultado()
    
def dividir():
        resultado.set(CFloat(Numero1.get()) / CFloat(Numero2.get()))
        mostrarresultado()
    
def mostrarresultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es : {resultado.get()}")
    Numero1.set("")
    Numero2.set("")


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

Button(marco, text="Sumar", command=sumar).pack(side="left", fill= X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left",fill= X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill= X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill= X, expand=YES)

ventana.mainloop()
