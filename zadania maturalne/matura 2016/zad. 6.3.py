plik = open('dane_6_3.txt', 'r')
linijki = plik.readlines()

for i in linijki:
    i = i.strip().split()
    klucz = 26 - abs(ord(i[0][0]) - ord(i[1][0]))
    for k in range(len(i[0])):
        if 26 - abs(ord(i[0][k]) - ord(i[1][k])) != klucz and abs(ord(i[0][k]) - ord(i[1][k])) != klucz:
            print(i[0])
            break
plik.close()