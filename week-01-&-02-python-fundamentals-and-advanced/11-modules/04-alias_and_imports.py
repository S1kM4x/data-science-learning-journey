
# toda la libreria
import math # Esta libreria tiene funciones matematicas
print(math.sqrt(16)) # Aqui se esta ejecutando para sacar la raiz de 16

# Importar función específica
from datetime import datetime
print(datetime.now())

# Importar con alias
import random as r
print(r.randint(1, 10))

# importacion especifica
from math import sin, cos, pi
print(sin(pi/2))
print(cos(0))

# importacion de toda la libreria se agrega *, 
# la funcion menos recomendada ya que hara el codigo demasiado pesado
from math import *
print(sqrt(25))