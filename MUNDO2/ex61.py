primeiro = int(input("Digite o 1ª termo da P.A. : "))
razao = int(input("Digite a razao da P.A. : "))
termos=0
while termos<11:
    resultado=primeiro+termos*razao
    termos+=1
    print(resultado)

print("Acabou")

