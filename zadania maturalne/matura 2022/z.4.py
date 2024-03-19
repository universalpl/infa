plik = open('liczby.txt', 'r')
wyniki = open('wyniki4.txt', 'w')
trojki = open('trojki.txt', 'w')
def zad41(p, w):
    linijki = p.readlines()
    s = 0
    k = 0
    for i in linijki:
        i = i.strip()
        if i[0] == i[-1]:
            s += 1
            if k == 0:
                w.write(f'Pierwsza: {i}')
                w.write('\n')
                k += 1
    w.write(f'Liczb z pierwsza cyfra rowna ostatniej: {str(s)}')
    w.write('\n')
    p.seek(0)
    return ()
zad41(plik, wyniki)
def rozklad(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n = n // k
            czynniki.append(k)
        k += 1

    return czynniki


def zad42(p, w):
    pop = 0    #poprzednia
    lista = []
    linijki = p.readlines()
    for i in linijki:
        i = i.strip()
        i = int(i)
        if len(rozklad(i)) > pop:
            pop = len(rozklad(i))
    for i in linijki:
        i = i.strip()
        i = int(i)
        if len(rozklad(i)) == pop:
            lista.append(i)
    w.write(str(pop))
    w.write(' ')
    w.write(str(lista))
    w.write(' ')
    najw = 0
    najwr = 0   #najwiekszy rozklad
    for i in linijki:
        i = i.strip()
        i = int(i)
        z = set(rozklad(i))
        if len(z) == len(rozklad(i)) and len(z) > najw:
            najw = len(z)
            najwr = i
    w.write(str(najw))
    w.write(' ')
    w.write(str(najwr))
    w.write('\n')
    p.seek(0)
    return ()


zad42(plik, wyniki)

def zad43a(p, w):    #trójki
    t = 0
    linijki = p.readlines()
    for i in linijki:
        i = i.strip()
        i = int(i)
        for k in linijki:
            k.strip()
            k = int(k)
            if i == k:
                pass
            elif k % i == 0:
                for x in linijki:
                    x = x.strip()
                    x = int(x)
                    if x == k:
                        pass
                    elif x % k == 0:
                        t += 1
                        w.write(str(i))
                        w.write(' ')
                        w.write(str(k))
                        w.write(' ')
                        w.write(str(x))
                        w.write('\n')
    w.write(f'Jest {t} trojek')
    w.write('\n')
    plik.seek(0)


zad43a(plik, trojki)


def zad43b(p, w):
    piatki = 0
    linijki = p.readlines()
    for i in linijki:
        i = i.strip()
        i = int(i)
        for k in linijki:
            k.strip()
            k = int(k)
            if i == k:
                pass
            elif k % i == 0:
                for x in linijki:
                    x = x.strip()
                    x = int(x)
                    if x == k:
                        pass
                    elif x % k == 0:
                        for y in linijki:
                            y = y.strip()
                            y = int(y)
                            if y == x:
                                pass
                            elif y % x == 0:
                                for z in linijki:
                                    z = z.strip()
                                    z = int(z)
                                    if z == y:
                                        pass
                                    elif z % y == 0:
                                        piatki += 1
    w.write(f'Jest {piatki} piatek')
    plik.seek(0)


zad43b(plik, trojki)


plik.close()
wyniki.close()
