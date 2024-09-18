n = int(input("Informe um número: "))

produto = 1                     # Elemento neutro da multiplicação
i = n

while i > 0:
    produto = produto * i       # Acumulação da multiplicação
    i = i -1

print("O resultado é", produto)