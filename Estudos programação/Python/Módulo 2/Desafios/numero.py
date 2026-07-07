import random 

print("======DESAFIO ACERTE O NÚMERO======")

num = random.randint(1,100)
respostas = 0
tentativas = 0

while (num != respostas):
    tentativas +=1
    respostas = int(input("Digite o número: "))
    
    if (respostas > num):
        print("O número é menor!")
    elif (respostas < num):
        print("O número é maior!")

print(f"Você acertou o número é {num} e você precisou de {tentativas} tentativas para acertar")
