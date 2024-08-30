n = int(input("Informe um número: "))

produto = 1 # Elemento neutro

for e in range(n, 0, -1):
    produto = produto * e

print(produto)