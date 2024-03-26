velocidade = float(input("A velocidade do carro em Km é: "))
velocidadeMaxima=80
multa=(velocidade-velocidadeMaxima)*7
if velocidade > 80:
    print("Você ultrapassou a velocidade permitida de 80Km/h. Você será multado em R$ {:.2f}.".format(multa))
print("Tudo ok!")

