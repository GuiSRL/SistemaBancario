# Passo 01: Criar variáveis para representar o saldo e a opção do menu
saldo = 0.0 # Saldo inicial (você pode alterar este valor)
opcao = 0

# Passo 02: Exibir uma mensagem de boas-vindas e as opções do menu
print("Olá! Bem vindo ao seu banco virtual")
print("----------------------------------.")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")
print("----------------------------------.")

# Passo 03: Ler a opção do usuário
opcao_str = input("Digite a opção desejada: ")

# Passo 04: Validar a opção do usuário usando um laço while
while not opcao_str.isdigit() or not (1 <= opcao <= 4):
    print("Opcao invalida. Por favor, digite uma opcao valida.")
    opcao_str = input("Digite a opcao desejada: ")

    opcao = int(opcao_str)

# Aqui você pode adicionar a lógica para cada opção do menu
if opcao == 1:
    print(f"Seu saldo é de R$ {saldo:.2f}")
elif opcao == 2:
    valor_str = input("Digite o valor depositado: ")
    valor = float(valor_str)
    saldo += valor
    print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
elif opcao == 3:
    valor_saque = input("Digite o valor a sacar: R$ ")
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")
elif opcao == 4:
    print("Obrigado por utilizar nosso banco virtual!")