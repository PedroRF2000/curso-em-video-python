reta1 = float(input("Informe o comprimento em cm da 1ª reta: "))
reta2 = float(input("Informe o comprimento em cm da 3ª reta: "))
reta3 = float(input("Informe o comprimento em cm da 2ª reta: "))
if reta2+reta3>reta1 and reta1+reta3>reta2 and reta1+reta2>reta3:
    print("Pode formar um triângulo!")
else:
    print("Não pode formar um triângulo!")
    