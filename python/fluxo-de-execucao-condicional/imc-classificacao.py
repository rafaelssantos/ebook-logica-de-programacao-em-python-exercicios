altura = float(input("Qual é a sua altura? "))
peso = float(input("Qual é o seu peso? "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc <= 25:
    print("Peso normal.")
elif 25 < imc <= 30:
    print("Acima do peso.")
else:
    print("Obesidade")