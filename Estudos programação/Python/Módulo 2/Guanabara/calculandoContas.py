casa = float(input("Qual o preço da casa? "))
salary = float(input("Salário do comprador? "))
age = int(input("Quantos anos você quer pagar? "))

total = casa/age
meses = age*12

if total > salary+700:
    print(f"Você quer comprar uma casa de R${casa} e quer pagar em {age}, então a prestação vai ser de R${total:2f}. Emprestimeo NEGADO")

else:
    print(f"Você quer comprar uma casa de R${casa} e quer pagar em {age}, então a prestação vai ser de R${total}. Emprestimeo ACEITO")