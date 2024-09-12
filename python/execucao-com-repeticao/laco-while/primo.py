num = int(input("Informe um número: "))
i = 1
cont_divisores = 0

while i <= num:
    if num % i == 0:
        cont_divisores = cont_divisores + 1
    if cont_divisores >= 3:     # Não precisa continuar verificação porque já sabemos que não é primo
        break
    i = i + 1

if cont_divisores == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")