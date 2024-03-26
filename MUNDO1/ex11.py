# Desafio 11:
largura = float(input("Informe a largura da parede em metros: "))
altura = float(input("Informe a altura da parede em metros: "))
areaParede = largura*altura
qtdTinta = areaParede/2
print("A qtd de litros de tinta necessária para pintar {} metros quadrados de parede é de {} litros.".format(
    areaParede, qtdTinta))
