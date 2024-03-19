plik = open('bin.txt', 'r')
linijki = plik.readlines()
pop = 0
for i in linijki:
    i = i.strip()
    if int(i) > int(pop):
        pop = i

print(pop)

plik.close()
