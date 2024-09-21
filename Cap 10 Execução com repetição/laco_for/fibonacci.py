n = int(input("Qual elemento da sequência de Fibonacci? "))

if n == 1 or n == 2:
    atual = 1
    print(atual)
else:
    ultimo = 1
    penultimo = 1
    for e in range(2, n):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
    print(atual)