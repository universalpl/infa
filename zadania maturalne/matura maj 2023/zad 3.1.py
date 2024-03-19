plik = open('pi.txt', 'r')
linijki = plik.readlines()
l = []
for i in linijki:
    i = i.strip()
    l.append(int(i))
z = 0

odp = 0
for i in l:
    if z > 0:
        print(pop)
        s = str(pop) + str(i)
        print(s)
        if int(s) > 90:
            odp += 1
        print(i)
    pop = i
    z += 1
print(odp)
plik.close()