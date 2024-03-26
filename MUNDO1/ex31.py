distância = float(input("Informe a distância da viagem em Km: "))
if distância <= 200:
    print("O valor da passagem será de R$ {:.2f}".format(distância*0.5))
else:
    print("O valor da passagem será de R$ {:.2f}".format(distância*0.45))
