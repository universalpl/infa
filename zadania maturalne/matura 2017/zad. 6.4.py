plik = open('dane.txt', 'r')
linijki = plik.readlines()

l = []
for i in linijki:
    i = i.strip().split()
    l.append([int(x) for x in i])

pow = 0
maks = [0]
i = 0
for k in range(len(l[i])):
    for i in range(len(l)):
        try:
            if l[i][k] == l[i + 1][k]:
                maks[pow] += 1
            else:
                maks.append(0)
                pow += 1
                maks[pow] += 1
        except IndexError:
            pass

print(maks)
print(max(maks))







plik.close()


