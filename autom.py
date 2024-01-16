import automBeolvas

def harmadik():
    kocsi = []
    befajl = open("auto.txt", "r", encoding="utf-8")
    befajl.readline()
    sorok = befajl.readlines()

    for index in range(0, len(sorok), 1):
        aktSor = sorok[index].strip().split("$")
        auto = automBeolvas.Osztaly(aktSor[0], aktSor[1])

        kocsi.append(auto)
        befajl.close()
        return kocsi


def tabla(kocsi):
    print(f"{kocsi}")

def flotta():
    pass


def ertekeles():
    pass

def kiir():
    pass