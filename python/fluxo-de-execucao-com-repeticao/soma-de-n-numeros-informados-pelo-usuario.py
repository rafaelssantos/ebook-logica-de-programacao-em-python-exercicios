n = int(input("Quantidade de números a somar: "))

soma = 0    # 0 é o elemento neutro da soma
for e in range(n):
    num = int(input("Informe o número: "))
    soma = soma + num
print("Resultado:", soma)