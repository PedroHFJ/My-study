print("""
===============================
        PROGESSÃO ARTMÉTICA
===============================
""")

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
resultado =primeiro

for i in range(10):
    print(f"{resultado}", end=" --> ")
    resultado += razao