salario_bruto = float(input("Informe o salário bruto: "))
inss = 0

if salario_bruto <= 1412:   # 7,5%
    inss = salario_bruto * 0.075
elif 1412.01 <= salario_bruto <= 2666.68: # 9%
    faixa_salario = salario_bruto - 1412.01
    inss = faixa_salario * 0.09 + 1412 * 0.075
elif 2666.69 <= salario_bruto <= 4000.03: # 12%
    faixa_salario = salario_bruto - 2666.69
    inss = faixa_salario * 0.12 + 1254.67 * 0.09 + 1412 * 0.075
elif 4000.04 <= salario_bruto <= 7786.02: # 14%
    faixa_salario = salario_bruto - 4000.04
    inss = faixa_salario * 0.14 + 1333.34 * 0.12 + 1254.67 * 0.09 + 1412 * 0.075
else:
    inss = 3785.98 * 0.14  + 1333.34 * 0.12 + 1254.67 * 0.09 + 1412 * 0.075

salario_tributavel = salario_bruto - inss

imposto = 0
if salario_tributavel <= 2259.20 :
    imposto = 0 # Isento
elif 2259.21 <= salario_tributavel <= 2826.65:
    imposto = salario_tributavel * 0.075 - 169.44
elif 2826.66 <= salario_tributavel <= 3751.05:
    imposto = salario_tributavel * 0.15 - 381.44
elif 3751.06 <= salario_tributavel <= 4664.68:
    imposto = salario_tributavel * 0.225 - 662.77
else:
    imposto = salario_tributavel * 0.275 - 896

salario_liquido = salario_tributavel - imposto

print("Salário bruto R$", f"{salario_bruto:.2f}")
print("INSS R$", f"{inss:.2f}") 
print("Salário tributável R$ ", f"{salario_tributavel:.2f}")
print("IRPF R$", f"{imposto:.2f}")
print("Salário líquido R$", f"{salario_liquido:.2f}")