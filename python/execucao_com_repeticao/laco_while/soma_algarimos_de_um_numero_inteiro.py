num = int(input("Informe um número: "))

soma = 0
while num != 0:
    resto = num % 10
    num = num // 10
    soma = soma + resto

print("A soma dos algarismos é", soma)
