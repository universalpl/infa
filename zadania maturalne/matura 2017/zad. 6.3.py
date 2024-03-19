plik = open('dane.txt', 'r')
linijki = plik.readlines()

l = []
licznik = 0
for i in linijki:
    i = i.strip().split()
    l.append(i)
kont = []
zmienna = 0
licz = 0

for listain in range(len(l)):

    for indeks in range(len(l[listain])):
        try:
            if abs(int(l[listain][indeks]) - int(l[listain][indeks + 1])) > 128:
                if [listain, indeks] in kont and [listain, indeks + 1] not in kont:
                    licz += 1
                elif [listain, indeks] not in kont and [listain, indeks + 1] in kont:
                    licz += 1
                elif [listain, indeks] in kont and [listain, indeks + 1] in kont:
                    pass
                else:
                    licz += 2
                kont.append([listain, indeks])
                kont.append([listain, indeks + 1])

            if abs(int(l[listain][indeks]) - int(l[listain + 1][indeks])) > 128:
                if [listain, indeks] in kont and [listain + 1, indeks] not in kont:
                    licz += 1
                elif [listain + 1, indeks] in kont and [listain, indeks] not in kont:
                    licz += 1
                elif [listain, indeks] in kont and [listain + 1, indeks] in kont:
                    pass
                else:
                    licz += 2
                kont.append([listain, indeks])
                kont.append([listain + 1, indeks])
        except:
            pass
        indeks += 1

    listain += 1

print(licz)

plik.close()



# plik = open('dane.txt', 'r')
# linijki = plik.readlines()
#
# l = []
# licznik = 0
# for i in linijki:
#     i = i.strip().split()
#     l.append(i)
# kont = []
# zmienna = 0
# licz = 0
# listain = 0
# for i in l:
#     indeks = 0
#     for k in i:
#         try:
#             if abs(int(l[listain][indeks]) - int(l[listain][indeks + 1])) > 128:
#                 if [listain, indeks] in kont and [listain, indeks + 1] not in kont:
#                     licz += 1
#                 elif [listain, indeks] not in kont and [listain, indeks + 1] in kont:
#                     licz += 1
#                 elif [listain, indeks] in kont and [listain, indeks + 1] in kont:
#                     pass
#                 else:
#                     licz += 2
#                 kont.append([listain, indeks])
#                 kont.append([listain, indeks + 1])
#
#             if abs(int(l[listain][indeks]) - int(l[listain + 1][indeks])) > 128:
#                 if [listain, indeks] in kont and [listain + 1, indeks] not in kont:
#                     licz += 1
#                 elif [listain + 1, indeks] in kont and [listain, indeks] not in kont:
#                     licz += 1
#                 elif [listain, indeks] in kont and [listain + 1, indeks] in kont:
#                     pass
#                 else:
#                     licz += 2
#                 kont.append([listain, indeks])
#                 kont.append([listain + 1, indeks])
#         except:
#             pass
#         indeks += 1
#
#     listain += 1
#
# print(licz)
#
# plik.close()