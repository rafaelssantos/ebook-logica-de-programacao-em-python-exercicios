valor_compra = float(input("Informe o valor da compra: "))

print("Escolha a opção de crédito")
print("1 - à vista")
print("2 - a prazo")

opcao = int(input("Opção: "))
if opcao == 1:
    desconto = valor_compra * 0.1                                   # 10% é equivalente ao decimal 0,1
    valor_a_pagar = valor_compra - desconto
    print(f"Valor a pagar R$ {valor_a_pagar:.2f}")                  # Resultado com f-string (Opção 1)
    print("Valor a pagar R$", valor_a_pagar)                        # Resultado com string (Opção 2)
elif opcao == 2:
    qtde_parcelas = int(input("Informe o número de parcelas"))
    valor_parcela = valor_compra / qtde_parcelas
    print("{qtde_parcelas} parcelas de R$ {valor_parcela:.2f}")     # Resultado com f-string (Opção 1)
    print(qtde_parcelas, "parcelas de R$", valor_parcela)           # Resultado com string (Opção 2)
else:
    print("Opção inválida")