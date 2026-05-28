try:
    num = int(input("Digite o número para conversão: "))

    print("""
Escolha uma das opções para a conversão
[1] Número binário
[2] Número Octal
[3] Número Hexadecimal
""")

    escolha = int(input("Digite a sua escolha: "))

    if(escolha == 1):
        print(f"O número {num} convertido em binário é {bin(num)}")
    elif(escolha ==2):
        print(f"O seu número{num} convertido em octal é {oct(num)}")
    elif(escolha == 3):
        print(f"O seu número {num} convertido em hexadecimal é  {hex(num)}")
    else:
        print("Número inválido!")

except ValueError:
    print("Você digitou um número invalido!")



