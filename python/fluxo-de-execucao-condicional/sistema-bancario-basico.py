conta = input("Informe o número da conta: ")

if conta == "858585-8":
    senha = input("Informe a sua senha: ")
    if senha == "54321":
        print("Bem-vindo!")
        print("1 - Mostrar saldo")
        print("2 - Fazer um saque")
        print("3 - Fazer um depósito")
        print("4 - Sair")
        opcao = int(input("Informe a opção: "))
        saldo = 500
        if opcao == 1:                                                  #Saldo
            print("Seu saldo é de R$", saldo)
            print(f"Seu saldo é de R$ {saldo:.2f}")
        elif opcao == 2:                                                #Saque
            saque = float(input("Informe o valor do saque "))
            if saque <= saldo:
                saldo = saldo - saque
                print("Saldo atualizado R$", saldo)
                print(f"Saldo atualizado R$ {saldo:.2f}")
            else:
                print("Saldo indisponível")
        elif opcao == 3:                                                #Deposito
            deposito = float(input("Informe o valor do deposito: "))
            saldo = saldo + deposito
            print("Saldo atualizado R$", saldo)
            print(f"Saldo atualizado R$ {saldo:.2f}")
        elif opcao == 4:                                                # Sair
            print("Obrigado por usar nosso banco.")
        else: #Inválido
            print("Opção inválida.")
    else:
        print("Senha inválida!")
else:
    print("Número da conta inválido.") 