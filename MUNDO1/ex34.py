salario = float(input("Informe o valor do seu salário: "))
if salario > 1250:
    print("O seu novo salário será de R$ {:.2f} , um aumento de 10% .".format(salario+(salario*10/100)))
else:
    print("O seu novo salário será de R$ {:.2f} , um aumento de 15% .".format(salario+(salario*15/100)))
