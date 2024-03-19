plik = open('przyklad.txt', 'r')
linijki = plik.readlines()

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


liczby = []
for i in linijki:
    i = i.strip()
    liczby.append(int(i))

max_dlugosc = 0
max_start = 0
max_nwd = 0

start = 0
nwd_aktualny = liczby[0]
dlugosc = 1

for i in range(1, len(liczby)):
    nwd_aktualny = nwd(nwd_aktualny, liczby[i])
    if nwd_aktualny == 1:
        start = i
        nwd_aktualny = liczby[i]
        dlugosc = 1
    else:
        dlugosc += 1
        if dlugosc > max_dlugosc:
            max_dlugosc = dlugosc
            max_start = start
            max_nwd = nwd_aktualny

print(liczby[max_start], max_dlugosc, max_nwd)


plik.close()