plik = open('bin.txt', 'r')
wyniki = open('wyniki5.txt', 'w')

def xor5(a):
    x = int(str(a), base = 2)
    x = x//2
    x = bin(x)
    x = x[2:]
    x = str(x)
    a = str(a)
    a = list(a)
    x = list(x)
    if len(x) != len(a):
        if len(x) < len(a):
            r = len(a) - len(x)
            k = 0
            while k != r:
                x.insert(0, '0')
                k += 1

        elif len(x) > len(a):
            r = len(x) - len(a)
            k = 0
            while k != r:
                a.insert(0, '0')
                k += 1
    k = 0
    p = ''
    for i in a:
        if i == '1' and x[k] == '1':
            p += '0'
        elif i == '1' and x[k] == '0' or i == '0' and x[k] == '1':
            p += '1'
        else:
            p += '0'
        k += 1
    z = 0
    for f in p:
        if f != '0':
            break
        z += 1
    p = p.replace('0', '', z)

    return p


linijki = plik.readlines()
for i in linijki:
    i = i.strip()
    print(xor5(i))
    wyniki.write(xor5(i))
    wyniki.write('\n')



plik.close()