qtde = None         #   A variável pode ser inicializada com qualquer valor
soma = 0

while qtde != "fim":
    qtde = input("Insira a quantidade ou fim: ")
    if qtde != "fim":
        valor = float(input("Insira o valor do produto: "))
        total_produto = int(qtde) * valor
        soma = soma + total_produto

print("Total da compra:", soma)