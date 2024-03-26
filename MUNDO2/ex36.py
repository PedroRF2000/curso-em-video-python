casa = float(input("Qual o valor da casa? R$"))
salário = float(input("Quanto é a sua renda mensal? R$"))
anos = int(input("Em quantos anos você vai pagar? "))
prestaçãoMensal = casa/(anos*12)
if prestaçãoMensal <= salário*30/100:
    print("O empréstimo foi aprovado!")
else:
    print("O empréstimo foi negado!")
