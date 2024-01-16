def elso():
    nev = input("Adja meg a felhasználónevét!")
    print("\t", end="")
    jelszo = input("Adja meg a jelszavát!")

    if nev == "bori99" and jelszo == "Szivecske<3":
        print("Belépés engedélyezve.")
    else:
        print("Belépés megtagadva.")
        return elso()