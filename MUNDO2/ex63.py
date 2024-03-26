sequencias = int(
    input("Vai querer saber que eu mostre quantos sequências de Fibonacci? "))
termo = 0
t1=0
t2=1
while termo <= sequencias:
    t3 = t1 + t2
    print(f"{t1}=>{t2}=>{t3}=>")
    termo+=1
    t1=t2
    t2=t3
print(f"{t1}=>{t2}=>{t3}=>")
print("Operação finalizada")
