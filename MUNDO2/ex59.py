maior = 0
desejo = 0
print("Você informará 2 valores e qual operação você deseja fazer com eles: ")
while desejo != 5:
    v1 = float(input("Informe o 1ª valor: "))
    v2 = float(input("Informe o 2ª valor: "))
    desejo = int(input(
        "Menu:\n[1]somar,\n[2]multiplicar,\n[3]maior,\n[4]novos números,\n[5]sair do programa. \nQual operação você deseja fazer com eles: "))
    soma = v1+v2
    mult = v1*v2
    if desejo == 1:
        print(f"A soma dos valores é {soma}")
    elif desejo == 2:
        print(f"A multiplicação dos valores é {mult}")
    elif desejo == 3:
        if v1 > v2:
            maior = v1
            print(f"O maior valor é {maior}")
        elif v2 > v1:
            maior = v2
            print(f"O maior valor é {maior}")
        else:
            print("Os dois números possuem o mesmo valor.")
    elif desejo == 4:
        print(f"O primeiro valor é {v1}\nE o segundo valor é {v2}")
    else:
        print("Número inválido, escolha uma número de 1 a 5")
print("Fim")
