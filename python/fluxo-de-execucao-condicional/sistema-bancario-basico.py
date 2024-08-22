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
        if opcao == 1:                                          # Operação de Saldo
            print("Seu saldo é de R$", saldo)                           # Impressão sem formatação (Opção 1)
            print(f"Seu saldo é de R$ {saldo:.2f}")                     # Impressão formatada para moeda (Opção 2)
        elif opcao == 2:                                        # Operação de Saque
            saque = float(input("Informe o valor do saque "))
            if saque <= saldo:
                saldo = saldo - saque
                print("Saldo atualizado R$", saldo)                     # Impressão sem formatação (Opção 1)
                print(f"Saldo atualizado R$ {saldo:.2f}")               # Impressão formatada para moeda (Opção 2)
            else:
                print("Saldo indisponível")
        elif opcao == 3:                                        # Operação de Depósito
            deposito = float(input("Informe o valor do deposito: "))
            saldo = saldo + deposito
            print("Saldo atualizado R$", saldo)                         # Impressão sem formatação (Opção 1)
            print(f"Saldo atualizado R$ {saldo:.2f}")                   # Impressão formatada para moeda (Opção 2)
        elif opcao == 4:                                         # Operação Sair
            print("Obrigado por usar nosso banco.")
        else: #Inválido
            print("Opção inválida.")
    else:
        print("Senha inválida!")
else:
    print("Número da conta inválido.") 