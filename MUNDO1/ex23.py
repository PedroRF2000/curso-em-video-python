numero = int(input("Digite um número de 0 a 9999: "))
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10
print("O número a ser analisado será {}".format(numero))
print("A unidade deste número é {}".format(u))
print("A dezena deste número é {}".format(d))
print("A centena deste número é {}".format(c))
print("O milhar deste número é {}".format(m))
