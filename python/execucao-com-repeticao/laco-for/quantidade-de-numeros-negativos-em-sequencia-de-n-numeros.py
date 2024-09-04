n = int(input("Informe a quantidade de números: "))

quantidade = 0          # 0 é o elemento neutro da contagem
for e in range(n):
    num = int(input("Informe um número: "))
    if num < 0:         # Condição que identificar um número negativo
        quantidade = quantidade + 1

print(quantidade)