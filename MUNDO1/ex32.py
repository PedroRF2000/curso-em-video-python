from calendar import isleap
ano = int(input("Digite o ano: "))
if isleap(ano):
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} não é bissexto!".format(ano))