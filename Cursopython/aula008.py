# Módulos 

# Duas maneiras básicas para importar bibliotecas 
# import --- ou from---import ----

# biblioteca math> matemática
# funções math > Ceil > arredondar pra cima , > Florr > arrendondar para baixo, > trunc> Eliminar da virgula para frente, > pow > ** potência, > sqrt > calcular raiz quadrada, > factorial> fatorial 
# No caso de só sqrt > from math import sqrt 

from math import sqrt , floor
num= int(input('DIGITE UM NÚEMRO:'))
raiz= sqrt(num)
print(' A raiz de {} é igual a {:.2f} ' .format(num, floor(raiz))) #ormat(num, math.ceil(raiz)))


# números aleatórios 
import random 
num= random.random
print(num)

