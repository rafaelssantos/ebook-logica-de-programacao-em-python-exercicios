n = int(input("Informe a quantidade de números: "))

qtde_par = 0
qtde_impar = 0
i = 0
while i < n:
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        qtde_par = qtde_par + 1
    else:
        qtde_impar = qtde_impar + 1
    i = i + 1

print("Quantidade de números pares:", qtde_par)
print("Quantidade de números ímpares:", qtde_impar)