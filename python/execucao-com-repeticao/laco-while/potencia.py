base =  int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))

produto = 1                         # Elementro neutro da multiplicação
for e in range(expoente):
    produto = produto * base        # Acumulação da multiplicação

print(produto)