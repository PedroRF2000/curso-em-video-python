from time import sleep
preçoNormal = float(input("O valor do produto deu: "))
sleep(2)
print(f"O valor da compra deu {preçoNormal}")
escolhaDePgto = input("Qual vai ser a escolha de pagamento? ")
formaDePgto = input("E qual será a forma de pagamento? ")

if escolhaDePgto == "a vista" and formaDePgto == "dinheiro" or formaDePgto == "cheque":
    print("O desconto será de 10%")
    print(f"O valor da compra com desconto será de {
          preçoNormal-(preçoNormal*10/100)}")
elif escolhaDePgto == "a vista" and formaDePgto == "cartão":
    print("O desconto será de 5%")
    print(f"O valor da compra com desconto será de {
          preçoNormal-(preçoNormal*5/100)}")
elif escolhaDePgto == "2x":
    print(f"O valor da compra com desconto será de {preçoNormal}")
else:
    print(f"O valor da compra com desconto será de {
          preçoNormal+(preçoNormal*20/100)}")
