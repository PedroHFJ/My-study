a = int(input("Digite um número: "))

for i in range(a):
    if(i%2 == 1):
        continue
    print(i)