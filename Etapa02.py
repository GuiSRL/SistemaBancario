saldo = 1000.0 #Saldo inicial  (você pode alterar este valor)

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é R$ {saldo:.2f}")

def sacar():
    """Realiza a operação de saque"""
    global saldo # Indica que estamos modificando a variável global SALDO
    valor_saque = float(input("Digite o valor a sacar: R$ "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
    else:
        print("Saldo insuficiente.")
    
def depositar():
    """Realiza a operação de depósito"""
    global saldo # Indica que estamos modificando a variável global SALDO
    valor_deposito = float(input("Digite o valor a depositar: R$ "))
    saldo += valor_deposito
    print(f"Deposito de R$ {valor_deposito:.2f} realizado com sucesso!")

# Exibir uma mensagem de boas-vindas e as opções do menu
print("Olá! Bem vindo ao seu banco virtual")
print("----------------------------------.")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")
print("----------------------------------.")

# Ler a opção do usuário
opcao_str = input("Digite a opção desejada: ")

# Validar a opção do usuário usando um laço while
while not opcao_str.isdigit() or not (1 <= opcao <= 4):
    print("Opcao invalida. Por favor, digite uma opcao valida.")
    opcao_str = input("Digite a opcao desejada: ")

    opcao = int(opcao_str)

# Executar a ação com base na opção do usuário
if opcao == 1:
    consultar_saldo()
elif opcao == 2:
    depositar()
elif opcao == 3:
    sacar()
elif opcao == 4:
    print("Obrigado por utilizar nosso banco virtual!")