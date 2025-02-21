# Objetivo geral

    # Separar funções existentes de saque, depósito e extrato em funções.

    # Criar duas novas funções:
        # - Cadastrar usuário (cliente)
        # - Cadastrar conta bancária

    # Além disso, criaremos funções separadas para:
        # - sacar
        # - depositar
        # - visualizar histórico

    # Também criaremos duas novas funções do sistema
        # - criar usuário (cliente do banco)
        # - criar conta corrente (vincular com usuário


# Função de Saque
    # Deve receber os argumentos apenas por nome (keyword only).
    # Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
    # Sugestão de retorno: saldo e extrato


# Função de Depósito
    # Deve receber os argumentos apenas por posição (positional only).
    # Sugestão de argumentos: saldo, valor, extrato
    # Sugestão de retorno: saldo e extrato


# Função de Extrato
    # Deve receber os argumentos por posição e nome (positional only e keyword only)
    # Argumentos posicionais: saldo, 
    # Argumentos nomeados: extrato


# Novas funções

    # Criar Usuário (cliente)
        # O programa deve armazenar os usuários em uma lista, um usuário composto por: nome, data de nascimento, cpf e endereço.
        # O endereço é uma string com o formato: logradouro, nro, bairro, cidade/sigla estado
        # Deve ser armazenado somente os números do CPF
        # Não podemos cadastrar 2 usuários com o mesmo CPF

    # Criar conta corrente 
        # O programa deve armazenar contas em uma lista, uma conta é composta por:
            # agência, número da conta e usuário
        # O número da conta é sequencial, iniciado em  1. 
        # O número da agência é fixo: "0001".
        # O usuário pode ter mais de 1 conta, mas uma conta pertence a somente um usuário

def depositar(saldo, valor, extrato, /):     # ---> positional only
    """Função para realizar depósito."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):      # ---> keyword only
    """Função para realizar saque."""
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor excede o limite de R$ 500,00 para saque.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):              # ---> positional only e keyword only
    print("\n======================= Extrato ======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================================")

def criar_usuario(usuarios):
    """Função para criar um novo usuário."""
    cpf = input("Informe o CPF (apenas números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário já cadastrado com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro, bairro, cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente(contas, usuarios):
    """Função para criar uma nova conta corrente."""
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if not usuario:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return
    
    numero_conta = len(contas) + 1
    contas.append({"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario})
    print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")

def main():
    total_usuarios = []
    total_contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    Bem-vindo ao sistema bancário!
    Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta
    [q] Sair
    
    => """

    while True:
        opcao = input(menu)
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            criar_usuario(total_usuarios)
        elif opcao == "c":
            criar_conta_corrente(total_contas, total_usuarios)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Operação inválida. Tente novamente.")

if __name__ == "__main__":
    main()
