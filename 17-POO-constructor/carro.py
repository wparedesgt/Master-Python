

class Carro:

    #Atributos o propiedades
    #Caracteristicas del Carro
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    asientos = 2

    soy_publico = "Hola, soy un atributo publico"
    ___soy_privado = "Hola soy un atributo privado"



    def __init__(self, color, marca, modelo, velocidad, caballaje, asientos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.asientos = asientos
    


    #Metodos son acciones que hace el objeto (funciones)
    def getPrivado(self):
        return self.___soy_privado
    

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

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = "---- Información del Carro"
        info += "\n Color :" + self.getColor()
        info += "\n Marca :" + self.getMarca()
        info += "\n Modelo :" + self.getModelo()
        info += "\n Velocidad :" + str(self.getVelocidad())

        return info

#fin de la classe
    

    