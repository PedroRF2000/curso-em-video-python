sacado = int(input("Quanto o(a) sr(a) pretende sacar? R$"))
total = sacado
ced = 50
totCed = 0

while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f"Serão entregues {totCed} cédulas de R${ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
