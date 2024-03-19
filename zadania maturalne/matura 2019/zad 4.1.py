import math
plik = open('liczby.txt', 'r')
linijki = plik.readlines()

licz = 0
for i in linijki:
    i = i.strip()
    i = int(i)
    if i == 1:
        licz += 1
    elif int(i) % 3 == 0:
        k = 0
        p = 0
        while k <= int(i):
            k = math.pow(3, p)
            p += 1
            if k == int(i):
                licz += 1

print(licz)

















plik.close()