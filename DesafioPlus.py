import datetime
import json
import os  # Importa os módulos OS para verificar a existência do arquivo

nome_arquivo = "banco_dados.json"  # Nome do arquivo para salvar os dados
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            saldo = dados.get("saldo", 1000.0)  # Carrega o saldo, usa 1000.0 como padrão senão encontrar
            extrato = dados.get("extrato", [])  # Carrega o extrato, usa [] como padrão
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados padrão.")
        saldo = 1000.0
        extrato = []
else:
    saldo = 1000.0  # Saldo inicial
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
        extrato.append({"data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"), "tipo": "Saque", "valor": valor_saque})
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
    extrato.append({"data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"), "tipo": "Deposito", "valor": valor_deposito})
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
            data_hora = transacao["data_hora"]
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

def transferir():
    """Realiza a operação de transferência, verificando saldo."""
    global saldo, extrato
    while True:
        try:
            conta_transferir = input("Digite o numero da conta do destinatário: ")
            valor_transferir = float(input("Digite o valor a transferir: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um numero.")
    if (valor_transferir <= saldo):
        saldo -= valor_transferir
        agora = datetime.datetime.now()
        extrato.append({"data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"), "tipo": "Saque", "valor": valor_transferir})
        print(f"Transferência de R$ {valor_transferir:.2f} realizado com sucesso para a conta {conta_transferir}")
        print(f"Seu novo saldo é de: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")

# ... (seu código principal com loop while)
while True:
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato")
    print("5 - Transferência")
    print("6 - Sair")
    
    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if (1 <= opcao <= 6):
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
    elif opcao == 5:
        transferir()
    elif opcao == 6: # Opção para sair
        print("Obrigado por utilizar nosso banco virtual!")
        break

# Salva o saldo e o extrato no arquivo antes de sair
try:
    with open(nome_arquivo, "w") as arquivo:
        json.dump({"saldo": saldo, "extrato": extrato}, arquivo, indent=4)  # Indentação para melhor leitura
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}.")