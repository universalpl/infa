plik = open('liczby.txt', 'r')
wyniki = open('wyniki3.txt', 'w')
#odp 764

def chuj(M, a, b):
    k = 0
    for x in range(0, M):
        if (a ** x) % M == b:
            k += 1
    if k > 0:
        return True
    else:
        return False
suma = 0
linijki = plik.readlines()
for i in linijki:
    l = i.split()
    if chuj(int(l[0]), int(l[1]), int(l[2])) == True:
        suma += 1

wyniki.write(str(suma))
plik.close()
wyniki.close()