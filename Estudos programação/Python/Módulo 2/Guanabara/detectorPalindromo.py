frase = str(input("Digite uma palavra ou frase: ")).strip().upper()
fraseFinal = frase.split()
junto = "".join(fraseFinal)
inverso = ''

for i in range(len(junto)-1,-1,-1):
    inverso += junto[i]

if (junto == inverso):
    print(f"A frase \"{junto}\" ao contrario é \"{inverso}\"")
    print("UMA FRASE PALÍNDROMA")

else:
    print(f"A frase \"{junto}\" ao contrario é \"{inverso}\"")
    print("Não é uma frase PALÍNDROMA")


