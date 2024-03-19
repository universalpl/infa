plik = open('NAPIS.TXT', 'r')
linijki = plik.readlines()

for i in linijki:
    i = i.strip()
    pop = 0
    dlugosc = len(i)
    liczk = 0
    for k in i:
        if ord(k) > pop:
            pop = ord(k)
            liczk += 1
    if liczk == dlugosc:
        print(i)
    liczk = 0
plik.close()