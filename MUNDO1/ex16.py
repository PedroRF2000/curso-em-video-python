# Desafio 16
import math

num = float(input("Informe o número real: "))
inteiro=round(num)
print("A porção inteira de {} é {}".format(num,inteiro))


# Outra forma de fazer este exercicio é

num = float(input("Informe o número real: "))
print("A porção inteira de {} é {}".format(num,int(num)))

# Outra forma de fazer este exercicio é

from math import trunc
num = float(input("Informe o número real: "))
inteiro=trunc(num)
print("A porção inteira de {} é {}".format(num,inteiro))
