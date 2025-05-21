import datetime

saldo = 1000.0 # Saldo inicial (você pode alterar este valor)
extrato = []  # Lista para armazenar as transações

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual e: R$ {saldo:.2f}")
    
def sacar():
    """Realiza a operação de saque, verificando saldo."""
    global saldo, extrato
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um numero.")
    if (valor_saque <= saldo):
        saldo -= valor_saque
        agora = datetime.datetime.now()
        extrato.append({"data_hora": agora, "tipo": "Saque", "valor": valor_saque})
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        print(f"Seu novo saldo é de: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito"""
    global saldo, extrato
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break # Sai do loop se a entrada for válida.
        except ValueError:
            print("Valor inválido. Por favor digite um numero.")
    saldo += valor_deposito
    agora = datetime.datetime.now()
    extrato.append({"data_hora": agora, "tipo": "Deposito", "valor": valor_deposito})
    print(f"Deposito de R$ {valor_deposito:.2f} realizado com sucesso!")
    print(f"Seu novo saldo e de: R$ {saldo:.2f}")


def exibir_extrato():
    """Exibe o extrato bancário"""
    global extrato
    if not extrato:
        print("Não foram realizadas transações")
    else:
        print("\n--- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

# ... (seu código principal com loop while)
while True:
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato")
    print("5 - Sair")
    
    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if (1 <= opcao <= 5):
                break # Sai do loop se a opção for válida
            else:
                print("Opcao invalida. Por favor, digite um numero entre 1 e 5.")
        except ValueError:
            print("Opcao invalida. Por favor, digite um numero inteiro.")
            
    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4: # nova condição para exibir extrato
        exibir_extrato()
    elif opcao == 5: # Opção para sair
        print("Obrigado por utilizar nosso banco virtual!")
        break