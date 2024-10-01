import geometria as geo

def main():
    print("CALCULADORA DA ÁREA DE POLÍGONOS")
    print("Este é um programa que cálcula a área de polígonos.")
    print("1 - Área do quadrado")
    print("2 - Área do retângulo")
    print("3 - Área do triângulo")
    print("4 - Área do círculo")

    opcao = int(input("Opção desejada: "))
    area = None
    if opcao == 1:
        lado = float(input("Informe o valor do lado: "))
        area = geo.area_quadrado(lado)
    elif opcao == 2:
        base = float(input("Informe o valor da base: "))
        altura = float(input("Informe o valor da altura: "))
        area = geo.area_retangulo(base, altura)
    elif opcao == 3:
        base = float(input("Informe o valor da base: "))
        altura = float(input("Informe o valor da altura: "))
        area = geo.area_triangulo(base, altura)
    elif opcao == 4:
        raio = float(input("Informe o valor do raio: "))
        area = geo.area_circulo(raio)
    else:
        print("Opção inválida!")
        
    
    if area != None:
        print("A área é", area)



if __name__ == "__main__":
    main()