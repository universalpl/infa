plik = open('pi.txt', 'r')
linijki = plik.readlines()
l = []
z = 0
for i in linijki:
    i = i.strip()
    if z > 0:
        s = str(pop) + str(i)
        l.append(s)
    pop = i
    z += 1
w = []
x = 0
for i in range(99):
    x += 1
    if x < 10:
        s = '0' + str(x)
        w.append((s))
    else:
        w.append(str(x))
w.insert(0, '00')

maks = 0
min = 999
f = ''
g = ''
for i in w:
    c = l.count(i)
    if c > maks:
        maks = c
        f = i
    if c < min:
        min = c
        g = i
print(f)
print(maks)
print(g)
print(min)



plik.close()