sexo = input(
    "Informe o seu sexo, 'Masculino' ou 'Feminino': ").strip().upper()[0]

while sexo not in "MF":
    sexo = input(
        "Sua resposta é incompatível com a nossa pergunta, tente novamente: ").strip().upper()[0]

if sexo == "M":
    print("O seu sexo é masculino.")
else:
    print("O seu sexo é feminino.")
