frase = input("Digite a sua frase: ").upper()
print("A letra 'a' aparece {} vezes.".format(frase.count("A")))
print("Ela aparece pela primeira vez na posição {} ".format(frase.find("A")+1))
print("Ela aparece pela última vez na posição {} ".format(frase.rfind("A")+1))
