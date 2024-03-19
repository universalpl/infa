plik = open('liczby.txt', 'r')
linijki = plik.readlines()

mala = linijki[0]
malaw = 0
duza = 0
duzaw = 0
wiersz = 1
for i in linijki:
    i = i.strip()
    if int(i) > int(duza):
        duza = i
        duzaw = wiersz
    if int(i) < int(mala):
        mala = i
        malaw = wiersz
    wiersz += 1

print(malaw, duzaw)
plik.close()