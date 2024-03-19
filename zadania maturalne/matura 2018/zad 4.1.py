plik = open('sygnaly.txt', 'r')


linijki = plik.readlines()

wynik = ''
licznik = 1
for i in linijki:
    i = i.strip()
    #print(i)
    if licznik % 40 == 0:
        #print(i[9])
        wynik += i[9]
    licznik += 1
plik.close()
print(wynik)
