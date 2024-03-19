plik = open('bin.txt', 'r')
linijki = plik.readlines()
wynikp = 0
for i in linijki:
    i = i.strip()
    pop = 2
    wynik = 0
    for k in i:
        if k != pop:
            #print(i)
            wynik += 1
        pop = k
    if wynik <= 2:
        wynikp += 1

print(wynikp)



plik.close()