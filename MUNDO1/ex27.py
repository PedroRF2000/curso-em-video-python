nome = input("Informe o seu nome completo: ").strip().split()

print("O seu primeiro nome é {}".format(nome[0]))

print("O seu sobrenome é {}".format(nome[len(nome)-1]))
