plik = open('przyklad.txt', 'r')
linijki = plik.readlines()

def czy_spelnia_warunek(lista):
    dlugosc = len(lista)
    for j in range(dlugosc - 1):
        for k in range(j + 1, dlugosc):
            znak1 = lista[j]
            znak2 = lista[k]

            liczba1 = ord(znak1)
            liczba2 = ord(znak2)
            if abs(liczba1 - liczba2) > 10:
                return False
    return True

for i in linijki:
    i = i.strip()
    dlugosc = len(i)
    litera = 1
    lista = list(i)
    if czy_spelnia_warunek(lista):
        print(i)


















plik.close()