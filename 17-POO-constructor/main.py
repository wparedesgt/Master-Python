
from carro import Carro

carro = Carro("Amarillo", "Renault", "Clio", 150, 200, 4)

print(carro.getColor())



carro = Carro("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Carro("Verde", "Seat", "panda", 240, 200, 4)
carro2 = Carro("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Carro("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado 

#carro3 = "Aleatorio"

if type(carro3) == Carro:
    print("Es un objeto correcto")
else:
    print("No es un objeto Correcto")

#Visibilidad

print(carro.soy_publico)
print(carro.getPrivado())




