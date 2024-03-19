plik = open('NAPIS.TXT', 'r')
linijki = plik.readlines()

licz = 0
for i in linijki:
    i = i.strip()
    suma = 0
    for k in i:
        suma += ord(k)
    pierwsza = 1
    suma = int(suma)
    for z in range(suma):    #ja wiem ze funkcja itd ale tak jest prosciej i to mi pierwsze przyszlo do glowy
        if z == 1 or z == suma or z == 0:
            pass
        elif suma % z == 0:
            pierwsza = 0
    if pierwsza == 1:
        licz += 1
    pierwsza = 0
print(licz)


plik.close()