n = int(input("Informe a quantidade de números: "))

quantidade = 0                          # Elemento neutro da contagem
for e in range(n):
    num = int(input("Informe um número: "))
    if num < 0:
        quantidade = quantidade + 1     # Acumulação da contagem

print(quantidade)