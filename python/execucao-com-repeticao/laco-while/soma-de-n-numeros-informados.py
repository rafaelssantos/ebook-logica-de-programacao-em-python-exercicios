n = int(input("Quantos elementos você deseja a somar? "))

i = 0
soma = 0
while i < n:
    num = int(input("Informe um número: "))
    soma = soma + num
    i = i + 1

print(soma)