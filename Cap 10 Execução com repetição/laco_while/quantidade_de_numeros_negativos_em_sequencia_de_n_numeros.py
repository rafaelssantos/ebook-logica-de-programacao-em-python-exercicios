n = int(input("Informe a quantidade de números: "))

quantidade = 0                          # Elemento neutro da contagem

i = 0
while i < n:
    num = int(input("Informe um número: "))
    if num < 0:
        quantidade = quantidade + 1     # Acumulação da contagem
    i = i + 1

print(quantidade)