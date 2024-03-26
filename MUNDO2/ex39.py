from datetime import date
anoDeNascimento = int(input("Informe o seu ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual-anoDeNascimento
if idade < 18:
    print(f"Você ainda vai se alistar! Ainda faltam {
          18-idade} anos para você se alistar.")
elif idade == 18:
    print("É a hora de se alistar!")
else:
    print(f"Já passou o tempo! Já se passou {idade-18} anos.")
