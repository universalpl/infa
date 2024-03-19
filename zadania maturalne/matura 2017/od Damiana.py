plik = open('dane.txt', 'r')
def zad6_3(plik):
    linijki = plik.readlines()
    liczby = [[int(n) for n in i.strip().split()] for i in linijki]
    wysokosc = 200
    szerokosc = 320
    max_roznica = 128
    kontrastujace = 0

    for y in range(wysokosc):
        for x in range(szerokosc):
            liczba = liczby[y][x]

            if x > 0:
                lewy = liczby[y][x - 1]
                if abs(lewy - liczba) > max_roznica:
                    kontrastujace += 1
                    continue

            if x < szerokosc - 1:
                prawy = liczby[y][x + 1]
                if abs(prawy - liczba) > max_roznica:
                    kontrastujace += 1
                    continue

            if y > 0:
                gorny = liczby[y - 1][x]
                if abs(gorny - liczba) > max_roznica:
                    kontrastujace += 1
                    continue

            if y < wysokosc - 1:
                dolny = liczby[y + 1][x]
                if abs(dolny - liczba) > max_roznica:
                    kontrastujace += 1
                    continue
            print(kontrastujace)
print(zad6_3(plik))
plik.close()