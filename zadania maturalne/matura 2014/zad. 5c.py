plik = open('NAPIS.TXT', 'r')
linijki = plik.readlines()
l = []
z = set()
for i in linijki:
    i = i.strip()
    l.append(i)

for i in l:
    if l.count(i) > 1:
        z.add(i)
print(z)

plik.close()