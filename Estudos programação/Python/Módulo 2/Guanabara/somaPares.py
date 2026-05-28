resultado = 0

for i in range(6):
    number = int(input("Digite um número: "))
    if (number%2 == 0):
        resultado += number
print(resultado)