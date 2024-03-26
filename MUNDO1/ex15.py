km=float(input("Quantos Km esse carro alugado percorreu?"))
dias=int(input("E por quantos ele já foi alugado?"))
valorPagar=0.15*km+60*dias
print("O valor a pagar pelo aluguel do carro é R$ {}".format(valorPagar))