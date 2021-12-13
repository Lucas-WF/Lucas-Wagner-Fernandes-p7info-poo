from models.cliente import Cliente
from models.conta import Conta
from models.saldo import Saldo

nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
idade = 20

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro")
        continue

cliente = Cliente(nome, endereco, idade)
conta = Conta(cliente)

i = 0

while True:
    user = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if i == 5:
        print("\nLimite de tentativas excedido!")
        break

    if conta.login(user, senha) == "Access":
        saldo = Saldo(conta, 1000)
        print("\nVocê tem:", saldo.renda, "R$")
        sair = True

        while sair:
            print("""\nDigite a sua operação:
            1 - Saque
            2 - Depósito
            3 - Sair \n""")

            try:
                op = int(input())
            except ValueError:
                print("Operação Inválida!")
                continue

            if op == 1:
                while True:
                    try:
                        valor = int(input("Agora digite o valor a ser retirado: "))
                        saldo.saque(valor)
                        print("\nVocê tem:", saldo.renda, "R$")
                        break
                    except ValueError:
                        print("Operação Inválida!")
                        break

            elif op == 2:
                while True:
                    try:
                        valor = int(input("Agora digite o valor a ser retirado: "))
                        saldo.deposito(valor)
                        print("\nVocê tem:", saldo.renda, "R$")
                        break
                    except ValueError:
                        print("Operação Inválida!")
                        break

            elif op == 3:
                sair = conta.sair(sair)
    else:
        print("\nTente novamente!\n")
        i += 1
        continue
