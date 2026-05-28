try:
    quantidade = int(input("Quantas provas você fez? "))
    media = 0
    for i in range(quantidade):
        i += 1
        prova = int(input(f"Digite a nota da {i}° prova: "))
        media +=prova

    notaFinal = media/quantidade
    if (notaFinal >= 6):
        print(f"A sua nota media foi {notaFinal}")
    elif(notaFinal < 6):
        print(f"Você reprovou a sua média foi {notaFinal}")
except  ValueError:
    print("Número inválido!")