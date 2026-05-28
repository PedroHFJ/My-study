print("======PAGAMENTO======")
valor = float(input("Qual foi o valor do pagamento? "))

print("""
[1] A vista no dinheiro
[2] A vista no cartão
[3] Em até 2x no cartão
[4] 3 ou mais vezes no cartão
""")
escolha = int(input("Escolha a opção: "))

if(escolha == 1):
    valorFinal = valor - (valor*0.10)
    print(f"O valor inicial era de R${valor} e ficou R${valorFinal}")
elif(escolha ==2):
    valorFinal = valor - (valor*0.05)
    print(f"O valor inicial era de R${valor} e ficou R${valorFinal}")
elif (escolha == 3):
    valorFinal = valor/2
    print(f"A parcela ficou R${valorFinal}, com zero desconto")
elif(escolha == 4):
    parcela = int(input("Quantas parcelas? "))
    if (parcela < 3):
        valorFinal = valor/2
        print(f"A parcela ficou R${valorFinal}, com zero desconto")
    elif(parcela >=3):
        valorFinal = valor + ((valor*0.20)*parcela)
        print(f"O valor a vista seria de R${valor}, mas com os juros ficou R${valorFinal}")
    