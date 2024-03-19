plik = open('liczby.txt', 'r')
linijki = plik.readlines()

licznik = 0
for i in linijki:
    i = i.strip()
    if i.count('0') > i.count('1'):
        licznik += 1

print(licznik)

plik.close()