saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = f"""
Saldo da Conta: R$ {saldo}

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação FALHOU! Valor informado invalido")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação FALHOU! Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print("Operação FALHOU! Você excedeu limite máximo por saque.")

        elif excedeu_saques:
            print("Operação FALHOU! Você excedeu o limite diario de saque.")
        
        elif valor > 0:            
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            

        else:
            print("Operação FALHOU! O valor informado é inválido.")

    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("========================================")

    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    