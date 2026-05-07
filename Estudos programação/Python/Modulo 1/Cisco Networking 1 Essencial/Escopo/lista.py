def lista(lista1):
    print(f"1° print {lista1}")
    print(f"2° print {lista2}")
    del lista2[0]
    print(f"3° print {lista1}")
    print(f"4° print {lista2}")

lista2 = [0,1,2]
lista(lista2)
print(f"5° print {lista2}")