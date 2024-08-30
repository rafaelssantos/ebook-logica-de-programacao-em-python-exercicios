n = int(input("Informe a quantidade de elementos"))

# Inicialização do menor elemento
menor = int(input("Informe o primeiro número: "))

for e in range(n-1):
    num = int(input("Informe o próximo número: "))
    if num < menor:
        menor = num

print(menor)