print("""
====================
    NÚMERO PRIMO
====================
""")

num = int(input("Digite um número: "))
primo = True
cont = 0

for i in range(num):
    i+=1
    if (num%i == 0):
        print(f"\033[1;33m{i}\033[m", end= " ")
        primo = False
        cont +=1
        if (cont <= 2):
            primo = True
    else:
        print(f"\033[0;31m {i}\033[m", end=" ")
if (primo == False):
    print(f"O seu número não é primo pois ele tem {cont} divisores")
else:
    print(f"O seu número é primo pois só tem dois divisores ( 1 e ele mesmo )")