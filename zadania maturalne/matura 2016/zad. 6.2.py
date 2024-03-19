plik = open('dane_6_2.txt', 'r')
linijki = plik.readlines()

str = ''

for i in linijki:
    i = i.strip().split()
    for k in i[0]:
        k = k.strip()
        try:
            if ord(k) - int(i[1]) % 26 < 65:
                k = chr(ord(k) + 26 - int(i[1]) % 26)
            else:
                k = chr(ord(k) - int(i[1]) % 26)
        except IndexError:
            pass
        str += k
    str += '\n'
print(str)

plik.close()