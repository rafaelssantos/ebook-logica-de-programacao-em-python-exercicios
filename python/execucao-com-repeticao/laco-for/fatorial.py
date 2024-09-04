n = int(input("Informe um número: "))

produto = 1                     # Elemento neutro da multiplicação

for e in range(n, 0, -1):
    produto = produto * e       # Acumulação da multiplicação

print(produto)