n = int(input("Informe o número de elementos: "))

quantidade = 0  # 0 é o elemento neutro da contagem
for e in range(n):
    num = int(input("Informe um número: "))
    if num < 0:
        quantidade = quantidade + 1

print(quantidade)