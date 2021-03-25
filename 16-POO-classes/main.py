# Programación orientada a objetos

# Definir una clase (molde para crear mas objetos de ese tipo)
# (Carro) con caracteristicas similares


class Carro:

    #Atributos o propiedades
    #Caracteristicas del Carro
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    asientos = 2

    #Metodos son acciones que hace el objeto (funciones)
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    


#fin de definicion de la classe

#Crear un objeto / Instanciar la clase

carro = Carro()

carro.setColor("amarillo")
carro.setModelo("murcielago")


print(carro)

print(carro.marca, carro.getModelo(), carro.getColor())

print("Velocidad actual: ", carro.velocidad )

carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()

print("Velocidad actual: ", carro.velocidad )

carro.frenar()

print("Velocidad nueva: ", carro.velocidad )


#Mejores opciones getter

print("Velocidad actual: ", carro.getVelocidad())


# Crear mas objetos

carro2 = Carro()
print(carro2.getColor())

carro2.setColor("Verde")
carro2.setModelo("Gallardo")


print(carro.getColor(), carro2.getColor(), carro.getModelo(), carro2.getModelo())







