cont = 0
while True:
    n = int(input("Informe o número que você deseja fazer a tabuada:"))
    if n < 0:
        break
    for cont in range(0, 11):
        +1
        print(f"{n}x{cont}={n*cont}")
    print("-"*30)
if n < 0:
    print("Número é negativo , valor informado é inválido.")
else:
    print("Operação encerrada.")
