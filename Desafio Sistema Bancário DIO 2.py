
def menu():
    menu = """\n
    =============== MENU ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
    ==>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
         print("Operação FALHOU! Valor informado invalido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
        print("Saque realizado com sucesso!")           

    else:
            print("Operação FALHOU! O valor informado é inválido.")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print("========================================")

def inserir_usuario(usuarios):
    cpf = input("Digite o cpf (apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuario já cadastrado no sistema.")
        return
            
    nome = input("Informe o nome do usuario: ")
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o Endereço (logradouro, numero, bairro, cidade, estado): ")
    usuarios.append({"cpf":cpf, "nome": nome, "nascimento":nascimento, "endereco":endereco})

    print("Parabens! Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """        
        print(linha)
    

def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)        

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )        

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            inserir_usuario(usuarios)

        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()