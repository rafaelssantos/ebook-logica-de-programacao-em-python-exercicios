n = int(input("Qual elemento da sequência de Fibonacci? "))

if n == 1 or n == 2:
    atual = 1
    print(atual)
else:
    ultimo = 1
    penultimo = 1
    i = 2
    while i < n:
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
        i = i + 1
    print(atual)