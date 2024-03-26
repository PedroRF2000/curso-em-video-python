from random import randint
vitoriasConsecutivas = 0
while True:
    jogador = input("Você vai querer ser ímpar ou par?").strip().upper()[0]
    if jogador == "I":
        computador = "P"
    else:
        computador = "I"
    print("Ímpar par!")
    maoJogador = int(input("Vou jogar o número:"))
    while maoJogador > 5:
        maoJogador = int(input("Só pode jogar com uma mão, jogue novamente:"))
    maoComputador = randint(0, 5)
    print(f"Você jogou {maoJogador} e o computador jogou {maoComputador}.")
    resultado = maoJogador+maoComputador

    if jogador == "P":
        if resultado % 2 == 0:
            print("Você venceu!")
            vitoriasConsecutivas += 1
        else:
            print("Você perdeu!")
            break
    elif jogador == "I":
        if resultado % 2 == 1:
            print("Você venceu!")
            vitoriasConsecutivas += 1
        else:
            print("Você perdeu!")
            break
print(f"Você obteve {
      vitoriasConsecutivas} vitórias consecutivas contra o seu oponente.")
