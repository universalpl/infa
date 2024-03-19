plik = open('liczby.txt', 'r')
linijki = plik.readlines()

dwa = 0
osiem = 0
for i in linijki:
    i = i.strip()
    if (int(i, base=2)) % 2 == 0:
        dwa += 1
    if (int(i, base=2)) % 8 == 0:
        osiem += 1

print(f'dwa: {dwa} osiem: {osiem}')
plik.close()
