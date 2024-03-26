contMaiores=contHomens=contMulheres=0
while True:
    idade = int(input("Informe a sua idade:"))
    sexo = input("Informe o seu sexo: [M/F]:").strip().upper()[0]
    while sexo not in "MF":
        sexo = input("Informe o seu sexo: [M/F]:").strip().upper()[0]
    if idade>17:
        contMaiores+=1
    if sexo=="M":
        contHomens+=1
    if sexo=="F" and idade<20:
        contMulheres+=1
    pergunta = input("Deseja continuar?[S/N]").strip().upper()[0]
    while pergunta not in "SN":
        pergunta = input("Deseja continuar?[S/N]").strip().upper()[0]
    if pergunta=="N":
        break
print(f"a) O número de pessoas com mais de 18 anos são {contMaiores}")
print(f"b) O número de homens cadastrados foram {contHomens}.")
print(f"c) O número de mulheres com menos de 20 anos são {contMulheres}")
