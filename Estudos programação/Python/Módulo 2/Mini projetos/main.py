import pyodbc

dados_conexao = (
    "DRIVER=DESKTOP-V7J4TVT;"
    "SERVER=;"
    "DATABASE=;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor =conexao.cursor()