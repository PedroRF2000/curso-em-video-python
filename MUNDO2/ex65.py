# pergunta = 'S'
cont = nTotal = media = maior = menor = 0
pergunta = input(
    "Você quer utilizar? [S/N]:").upper()
while pergunta == 'S':
    n = int(input("Digite o número: "))
    nTotal += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    pergunta = input(
        "Você quer continuar? [S/N]:").upper()
media = nTotal/cont
print(f"A média dos valores informados é de {media}\nO maior valor informado foi {maior}\nE o menor valor informado foi {menor}")
