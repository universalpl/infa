plik = open('przyklad.txt', 'r')
linijki = plik.readlines()

l = []
for i in linijki:
    i = i.strip().split()
    l.append([int(x) for x in i])

licz = 0
for listain in range(len(l)):
    for indeks in range(len(l[listain])):
        if ((indeks + 1 < len(l[listain]) and abs(l[listain][indeks] - l[listain][indeks + 1]) > 128) or
            (listain + 1 < len(l) and abs(l[listain][indeks] - l[listain + 1][indeks]) > 128) or
            (indeks - 1 >= 0 and abs(l[listain][indeks] - l[listain][indeks - 1]) > 128) or
            (listain - 1 >= 0 and abs(l[listain][indeks] - l[listain - 1][indeks]) > 128)):
            licz += 1

print(licz)

plik.close()