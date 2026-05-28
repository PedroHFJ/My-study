try:
    age = int(input("Digite o ano que você nasceu: "))
    idade = 2026-age
    anoDeAlistamento = 18 - idade

    if(18 < idade):
        print(f"Você já fez o seu alistamento, você tem {idade} anos")
    elif(18 == idade):
        print(f"Você precisa fazer o alistamento militar esse ano, pois você tem {idade} anos")
    elif(18 > idade):
        print(f"Você precisa fazer o alistamento militar em {2026+anoDeAlistamento}")
except ValueError:
    print("Número inválido")