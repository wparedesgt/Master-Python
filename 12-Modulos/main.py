"""
Un modulo son funcionalidades ya realizadas para utilizar.
En python ya existen muchos modulos consultarlos aqui:

https://docs.python.org/3/py-modindex.html

Podemos consultar o crear nuestros propios modulos
"""

import miModulo

print(miModulo.holaMundo("William Paredes"))
print(miModulo.calculadora(3,5,True))

from miModulo import holaMundo

print(holaMundo("William Paredes"))


# llamar a las funciones sin tener que llamar con el nombre del modulo

from miModulo import *


import numpy as np
import pandas as pd #Importar pandas

print(holaMundo("William Paredes"))
print(calculadora(3,5,True))


#Modulo de fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(f"Mi fecha personalizada: {fecha_personalizada}")

print(datetime.datetime.now().timestamp())

#Modulo de Matematicas

import math

print(f"Raiz cuadrada de 10: {math.sqrt(10)}")
print("Numero pi: ", float(math.pi))
print("Redondear: ", math.ceil(6.56798))
print("Redondear: ", math.floor(6.56798))

#Modulo random 

import random

print("Numero Aleatorio entre 15 y 67: ", random.randint(15,67))






