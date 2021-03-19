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


