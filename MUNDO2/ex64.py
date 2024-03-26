n=0
cont = 0
soma=0
n = int(input("Digite os números: "))
while n != 999:
    cont +=1
    soma=soma+n
    n = int(input("Digite os núm: [Caso queira parar o programa digite '999']"))
print(f"A qtde de números digitados foram de {cont} e a soma dos números informados foi de {soma}.")