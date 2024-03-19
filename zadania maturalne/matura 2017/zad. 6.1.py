plik = open('przyklad.txt', 'r')
linijki = plik.readlines()

maks = 0
minimum = 255
for i in linijki:
    i = i.strip().split()
    for j in i:
        if int(j) > maks:
            maks = int(j)
        if int(j) < minimum:
            minimum = int(j)
print(maks)
print(minimum)
plik.close()