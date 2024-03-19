plik = open('pary.txt', 'r')
linijki = plik.readlines()

for i in linijki:
    i = i.strip().split()
    i = i[1]
    pop = ''
    maks = [0, '']
    licz = 0
    for k in i:
        if k == pop:
            licz += 1
            if licz > maks[0]:
                maks[0] = licz
                maks[1] = k
        else:
            pop = k
            licz = 1
        if maks[0] == 0:
            maks[0] = 1
            maks[1] = i[0]
    print(maks[0] * maks[1], maks[0])

plik.close()