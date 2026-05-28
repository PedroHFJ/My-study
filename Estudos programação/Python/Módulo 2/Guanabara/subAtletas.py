age = int(input("Digite o seu ano de nascimento: "))

idade = 2026-age

if (idade < 13):
    print(f"""
Atleta MIRIM
idade: {idade}
""")
    
elif(idade > 13 and idade <=18):
    print("" \
    "Atleta JUNIOR" \
    f"idade: {idade}")

elif(idade > 18 and idade <40):
    print(f"""
Atleta ADULTO
idade: {idade}""")
    
elif(idade >= 40):
    print(f"""
Atleta VETERANO
idade: {idade}
""")