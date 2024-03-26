totCompra = qtde1000 = cont = maiorPreco = 0
produtoCaro = ""
while True:
    nome = input("Nome do produto: ")
    preço = float(input("Preço do produto: R$"))
    cont += 1
    totCompra += preço
    if preço > 1000:
        qtde1000 += 1
    if preço > 1000:
        maiorPreco = preço
        produtoCaro = nome
    pergunta = input("Vai querer continuar? [S/N]:").strip().upper()
    while pergunta not in "SN":
        pergunta = input("Vai querer continuar? [S/N]:").strip().upper()
    if pergunta == "N":
        break
print(f"a) O valor total da compra foi R$ {totCompra}.")
print(f"b) A qtde de produtos que custam mais de  R$ 1000,00 são {qtde1000} .")
print(f"a) O nome do produto mais caro foi {produtoCaro}, sendo que o seu valor foi R$ {maiorPreco}.")
