plik = open('pary.txt', 'r')
linijki = plik.readlines()

l = []
for i in linijki:
    i = i.strip().split()
    if int(i[0]) == len(i[1]):
        l.append(i)

lmin = 51
for i in l:
    if int(i[0]) < lmin:
        lmin = int(i[0])

for i in l:
    if int(i[0]) > lmin:
        l.pop(l.index(i))

print(min(l))


plik.close()