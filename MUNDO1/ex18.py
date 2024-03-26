# Desafio 18
from math import sin,cos,tan,radians
angulo=int(input("Informe o ângulo: "))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print("O seno do ângulo {} é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f} ".format(angulo,seno,cosseno,tangente))