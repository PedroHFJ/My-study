opcao = 0
saldo = 0
vlDeposito = 0
vlSaque = 0

nome = input("Digite o seu nome: ")
cpf = int(input("Digite o seu cpf: "))

while(opcao!=4):
    print("======Conta bancaria======")
    print("1-Depositar")
    print("2-Sacar")
    print("3-Exibir saldo")
    print("4-Sair")

    print()

    opcao = int(input("Escolha uma opção: "))   
    if(opcao>4):
        print("Opcao invalida")


    match opcao:
        case 1:
            vlDeposito = float(input("Digite o valor do deposito: ")) 
            saldo += vlDeposito


        case 2:
            vlSaque = float(input("Digite o valor do saque: "))
            if(saldo >=vlSaque):
                print("Saque realizado com sucesso!!!")
                saldo -= vlSaque
            else:
                print("Saldo insuficiente")

        case 3:
            print(nome, " saldo: ")
            print("R$",saldo)

    print()