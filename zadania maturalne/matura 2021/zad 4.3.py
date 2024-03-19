plik = open('instrukcje.txt', 'r')
linijki = plik.readlines()

l = []
for i in linijki:
    i = i.strip()
    i = i.split()
    if i[0] == 'DOPISZ':
        l.append(i[1])

print(l)
maks = 0
wyn = ''
for i in l:
    c = l.count(i)
    if c > maks:
        maks = c
        wyn = i
print(wyn, maks)










plik.close()