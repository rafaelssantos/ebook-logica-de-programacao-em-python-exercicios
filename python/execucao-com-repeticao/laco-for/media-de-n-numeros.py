n = int(input("Informe a quantidade de elementos: "))

soma = 0                # Elemento neutro da soma
for e in range(n):
    num = float(input("Informe um número: "))
    soma = soma + num   # Acumulação da soma

media = soma / n        # Divisão pela quantidade para calcular a média
print("Soma:", soma)
print("Média:", media)