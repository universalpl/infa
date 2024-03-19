#zamiana na bin
def binarna(n):
    l = []
    while n != 0:
        if n % 2 == 1:
            l.append(1)
            n = n//2
        elif n % 2 == 0:
            l.append(0)
            n = n//2
    l.reverse()
    return l


n = 67
n = binarna(n)
pop = 2
wynik = 0
for i in n:
    if i != pop:
        #print(i)
        wynik += 1
    pop = i
print(wynik)