import random

def ottelOszthato():
    lista = []
    otteloszthato = 0
    print("A lista elemei: ")
    print("\t", end="")
    for szamok in range(1, 51, 1):
        szam = random.randint(1, 100)
        lista.append(szam)
        if szam % 5 == 0:
            otteloszthato += 1
    for index in range(0, len(lista), 1):
        if index == len(lista) - 1:
            print(lista[index])
        else:
            print(f"{lista[index]} , ", end="")
    print(f"A listában {otteloszthato} darab öttel osztható szám van.")
    return lista
