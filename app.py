menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor a depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2F}\n"

        else:
            print("Valor inválido, por favor selecione novamente o valor a depositar")


    elif opcao == "s":
        valor = float(input("Valor a sacar: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo inválido, por favor selecione novamente o valor a sacar")

        elif excedeu_limite:
            print("Limite inválido, o valor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou, limite de saques inválidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2F}\n"
            numero_saques += 1

        else:
            print("Valor inválido, por favor selecione novamente o valor a sacar")
    
    
    elif opcao == "e":
        print("\n================ EXTRATO ===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")

