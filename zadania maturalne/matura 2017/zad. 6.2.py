plik = open('przyklad.txt', 'r')
linijki = plik.readlines()
licznik = 0
for i in linijki:
    i = i.strip().split()
    if i != i[::-1]:
        licznik += 1
print(licznik)

plik.close()