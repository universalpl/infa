plik = open('instrukcje.txt', 'r')
linijki = plik.readlines()
dopiszmax = 0
zmienmax = 0
usunmax = 0
przesunmax = 0
liczd = 0
liczz = 0
liczu = 0
liczp = 0
l = []
for i in linijki:
    i = i.strip()
    i = i.split()
    if i[0] == 'DOPISZ':
        liczz = liczu = liczp = 0
        liczd += 1
        if liczd > dopiszmax:
            dopiszmax = liczd
    elif i[0] == 'ZMIEN':
        liczd = liczu = liczp = 0
        liczz += 1
        if liczz > zmienmax:
            zmienmax = liczz
    elif i[0] == 'USUN':
        liczd = lcizz = liczp = 0
        liczu += 1
        if liczu > usunmax:
            usunmax = liczu
    elif i[0] == 'PRZESUN':
        liczd = liczz = liczu = 0
        liczp += 1
        if liczp > przesunmax:
            przesunmax = liczp
print(dopiszmax, zmienmax, usunmax, przesunmax)

plik.close()