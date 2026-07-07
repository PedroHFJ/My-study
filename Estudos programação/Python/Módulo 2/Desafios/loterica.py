print("======CAIXA======")

valor = int(input("Quanto você quer sacar? "))
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas1 = 0

while (valor >= 100):
    notas100 += 1
    valor -= 100
    

while(valor >= 50):
    notas50 += 1
    valor -= 50
    

while(valor >=10):
    notas10 +=1
    valor -=10
    

while(valor >= 5):
    notas5 += 1
    valor -=5
    

while (valor >=1):
    notas1 += 1
    valor -= 1

print(f"Foi preciso ({notas100}) nota de 100")
print(f"Foi preciso ({notas50}) nota de 50")
print(f"Foi preciso ({notas20}) nota de 20")
print(f"Foi preciso ({notas10}) nota de 10")
print(f"Foi preciso ({notas5}) nota de 5")
print(f"Foi preciso ({notas1}) nota de 1")


