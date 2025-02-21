# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python. Ele permite realizar operações básicas como depósitos, saques, exibição de extrato, criação de usuários e abertura de contas bancárias.

## Funcionalidades

- **Depósito**: Permite adicionar saldo à conta.
- **Saque**: Retira saldo da conta respeitando um limite diário.
- **Extrato**: Exibe as movimentações e o saldo da conta.
- **Criar Usuário**: Cadastra um novo usuário com nome, CPF, data de nascimento e endereço.
- **Criar Conta**: Cria uma conta associada a um usuário já cadastrado.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe ou copie o código para um arquivo `banco.py`.
3. No terminal ou prompt de comando, navegue até o diretório do arquivo e execute:
   ```bash
   python banco.py
   ```
4. O menu será exibido para interação.

## Regras do Sistema

- Cada usuário é identificado pelo CPF, e não pode haver duplicação de CPFs cadastrados.
- O limite máximo de saque por transação é de R$ 500,00.
- Há um limite de 3 saques diários por conta.
- O número da conta é sequencial e único para cada nova conta criada.
- A agência padrão para todas as contas é "0001".

## Exemplo de Uso

```
Bem-vindo ao sistema bancário!
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair

=>
```

O usuário pode selecionar uma opção digitando a letra correspondente e seguindo as instruções exibidas.

## Autor
Desenvolvido por Vinicius Silva.

