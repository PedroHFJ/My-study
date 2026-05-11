import requests

origemMoeda = "USD"
destinoMoeda = "BRL"

link = f" https://economia.awesomeapi.com.br/json/last/{origemMoeda}-{destinoMoeda}"

requisicao = requests.get(link)

cotacao = (requisicao.json()[f"{origemMoeda}{destinoMoeda}"]["bid"])

dolar = float(cotacao)

reais = float(input("Transformando real em dolar: "))

conversao = reais/dolar

print(f"Você vai ter ${conversao:.2f}")



