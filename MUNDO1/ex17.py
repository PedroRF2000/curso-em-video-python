from math import hypot
cateto_Oposto = float(
    input("Informe o valor do comprimento do cateto oposto em cm:"))
cateto_Adjacente = float(
    input("Informe o valor do comprimento do cateto adjacente em cm:"))
hipotenusa=hypot(cateto_Oposto,cateto_Adjacente)
print("O valor da hipotenusa deste triângulo é {:.1f} cm.".format(hipotenusa))