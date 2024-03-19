plik = open('liczby.txt', 'r')
linijki = plik.readlines()


def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1


licz = 0
for i in linijki:
    i = i.strip()
    i = str(i)
    z = 0
    for k in i:
        z += silnia(int(k))
    if z == int(i):
        print(i)
        licz += 1



plik.close()