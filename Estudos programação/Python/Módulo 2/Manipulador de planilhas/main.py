#Ler dados das planilhas
#Inserir cada célula de cada linha em um campo do sistema

import openpyxl


workBook = openpyxl.load_workbook('vendas_de_produtos.xlsx') #Ler arquivo excel 
vendasSheets = workBook["vendas"] #Identificar qual planilha é

for linha in vendasSheets.iter_rows(min_row=2): #Mostrar em qual linha começar a leitura
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)