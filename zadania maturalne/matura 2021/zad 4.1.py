plik = open('instrukcje.txt', 'r')
linijki = plik.readlines()

l = []
for i in linijki:
    i = i.strip()
    i = i.split()
    if i[0] == 'DOPISZ':
        l.append(i[1])
    elif i[0] == 'ZMIEN':
        l[-1] = i[1]
    elif i[0] == 'USUN':
        l.pop(-1)
    elif i[0] == 'PRZESUN':
        for k in l:
            if k == i[1]:
                if ord(k) == 90:
                    l[l.index(k)] = 'A'
                else:
                    o = ord(k)
                    l[l.index(k)] = chr((o + 1))
print(l)
print(len(l))

plik.close()