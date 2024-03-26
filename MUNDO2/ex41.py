from datetime import date
anoNascimento = int(input("O ano de nascimento do atleta é de: "))
anoAtual=date.today().year
idade=anoAtual-anoNascimento
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
