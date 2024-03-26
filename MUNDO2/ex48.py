soma=0
cont=0
for numeros in range (1,501):
    if numeros%2!=0 and numeros%3==0:
        cont=cont+1
        soma+=numeros
print(f"O número de valores que são ímpares e que são múltiplos de 3 são {cont}")
print(f"O valor da soma de todos os números ímpares múltiplos de 3 de 1 a 500 é igual a {soma}")

