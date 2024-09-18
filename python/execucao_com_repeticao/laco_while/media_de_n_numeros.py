n = int(input("Informe a quantidade de elementos: "))

soma = 0                # Elemento neutro da soma
i = 0
while i < n:
    num = float(input("Informe um número: "))
    soma = soma + num   # Acumulação da soma
    i = i + 1

media = soma / n        # Divisão pela quantidade para calcular a média
print("Soma:", soma)
print("Média:", media)