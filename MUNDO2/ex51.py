primeiro = int(input("Digite o 1ª termo da P.A. : "))
razao = int(input("Digite a razao da P.A. : "))
decimo = primeiro+(11-1)*razao
for i in range(primeiro, decimo, +razao):
    print(i)
print("Acabou")
