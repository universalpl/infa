plik = open('pary.txt', 'r')
linijki = plik.readlines()


def pierwsza(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <= 1:
        return False
    pierw = int(a**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if a % dzielnik == 0:
            return False
    return True


for i in linijki:
    i = i.strip().split()
    if int(i[0]) > 4 and int(i[0]) % 2 == 0:
        d = int(i[0])
        e = int(d/2)
        for k in range(e + 1):
            if k > 2 and pierwsza(k) and pierwsza(d - k):
                print(i[0], k, d - k)
                break

plik.close()