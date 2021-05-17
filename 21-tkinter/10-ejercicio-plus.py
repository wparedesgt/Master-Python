"""
CALCULADORA
    -Dos campos de texto
    -4 botones para las operaciones
    -Mostrar el resultado en una alerta
"""
class Calculadora:
    
    def __init__(self, alertas):
        self.Numero1 = StringVar()
        self.Numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def CFloat(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Inroduce Números")
        return result


    def sumar(self):
            self.resultado.set(self.CFloat(self.Numero1.get()) + self.CFloat(self.Numero2.get()))
            self.mostrarresultado()
        

    def restar(self):
            self.resultado.set(self.CFloat(self.Numero1.get()) - self.CFloat(self.Numero2.get()))
            self.mostrarresultado()
        
    def multiplicar(self):
            self.resultado.set(self.CFloat(self.Numero1.get()) * self.CFloat(self.Numero2.get()))
            self.mostrarresultado()
        
    def dividir(self):
            self.resultado.set(self.CFloat(self.Numero1.get()) / self.CFloat(self.Numero2.get()))
            self.mostrarresultado()
        

    def mostrarresultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operacion es : {self.resultado.get()}")
        self.Numero1.set("")
        self.Numero2.set("")


from tkinter import *
from tkinter import messagebox


ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

calculadora = Calculadora(messagebox)

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
Entry(marco, textvariable=calculadora.Numero1, justify=CENTER).pack()

Label(marco, text="Segundo Número: ").pack()
Entry(marco, textvariable=calculadora.Numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill= X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left",fill= X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill= X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill= X, expand=YES)

ventana.mainloop()