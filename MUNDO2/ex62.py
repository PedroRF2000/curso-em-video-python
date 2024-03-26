primeiro = int(input("Digite o 1ª termo da P.A. : "))
razao = int(input("Digite a razao da P.A. : "))
termos = 0
termosMaximos = int(input("Quantos termos você deseja saber desta P.A. ? "))
while termos < termosMaximos+1:
    resultado = primeiro+termos*razao
    termos += 1
    print(resultado)
print("Operação Finalizada")
