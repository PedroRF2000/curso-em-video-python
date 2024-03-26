from datetime import date

anoAtual = date.today().year
maioresIdade = 0
menoresIdade = 0

for i in range(0, 7):
    anoNascimento = int(input("Digite o seu ano de nascimento: "))
    if anoAtual - anoNascimento >= 18:
        maioresIdade += 1
    else:
        menoresIdade += 1
print(f"O número de jogadores maiores de idade são {
      maioresIdade} e menores são {menoresIdade}.")
