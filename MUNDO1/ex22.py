nome = input("Digite o seu nome: ")
print("O nome em maiusculo vai ser igual a  {}.".format(nome.upper()))
print("O nome em minusculo vai ser igual a {}.".format(nome.lower()))
print("Letras ao todo sem considerar espaços em brancos {}.".format(
    len(nome)-nome.count(" ")))
print("A contagem de letras do primeiro nome é {}.".format(nome.find(" ")))
