número = int(input("Digite um número inteiro qualquer: "))
baseDeCoversão = int(
    input("Qual será a base de conversão: aperte '1' para binário, '2' para octal e '3' para hexadecimal:"))

if baseDeCoversão == 1:
    print(f"A conversão para binário de {
          número} é igual a {bin(baseDeCoversão)}.")
elif baseDeCoversão == 2:
    print(f"A conversão para binário de {
          número} é igual a {oct(baseDeCoversão)}.")
elif baseDeCoversão == 3:
    print(f"A conversão para binário de {
          número} é igual a {hex(baseDeCoversão)} .")
else:
    print("Opção inválida tente novamente.")
