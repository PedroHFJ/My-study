import time
import random

print("======VAMOS JOGAR======")
print("""
[0] PAPEL
[1] TESOURA
[2] PEDRA
""")
 
jogada = int(input("Qual você vai escolher? "))

if (jogada == 0):
        resultado = "Papel"
elif(jogada == 1):
      resultado = "Tesoura"
elif(jogada == 2):
      resultado = "Pedra"

cpu = random.choice(["Tesoura", "Pedra", "Papel"])

if (jogada == cpu):
    print("JOKE")
    time.sleep(1)
    print("POW")
    time.sleep(1)
    print("Empate")

elif(jogada == 0 and cpu == "Pedra" or  jogada == 1 and cpu == "Papel" or jogada == 2 and cpu == "Tesoura"):
    print("JOKE")
    time.sleep(1)
    print("POW")
    time.sleep(2)

    print(f"VOCÊ GANHOU, você escolheu {resultado} e o computador {cpu}")
elif(jogada == 0 and cpu =="Tesoura" or jogada == 1 and cpu == "Pedra" or jogada == 2 and cpu == "Papel"):
    print("JOKE")
    time.sleep(1)
    print("POW")
    time.sleep(2)

    print(f"VOCÊ PERDEU, você escolheu {resultado} e o computador {cpu}")