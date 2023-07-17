menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor que você deseja depositar: "))
        if deposito > 0:
            print(f"Deposito de {deposito:.2f} efetuado")
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            saldo += deposito
            deposito = 0
        else:
            print("Valor invalido.")

    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Saque negado por ultrapassar o limite diario")
        elif saque > saldo:
            print("Saque negado, saldo insuficiente")
        elif saque > limite:
            print("Saque ultrapassa o limite maximo")
        else:
            print(f"Saque de {saque:.2f} efetuado")
            extrato += f"Saque: R$ {saque:.2f}\n"
            saldo -= saque
            numero_saques+=1
            saque = 0
                
    elif opcao == 3:
        print("============== EXTRATO ==============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")