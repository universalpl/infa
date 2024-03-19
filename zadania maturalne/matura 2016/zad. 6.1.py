plik = open('dane_6_1.txt', 'r')
linijki = plik.readlines()

str = ''
klucz = 107
for i in linijki:
    i = i.strip()
    for k in i:
        if ord(k) + klucz % 26 > 90:
            k = chr(ord(k) - 26 + klucz % 26)
        else:
            k = chr(ord(k) + klucz % 26)
        str += k
    str += '\n'
print(str)

plik.close()