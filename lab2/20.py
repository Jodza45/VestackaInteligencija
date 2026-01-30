# 20. Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja računa vrednost elementa
# u rezultujudem nizu korišdenjem 3 uzastopna elementa u nizu koji je prosleđen, korišdenjem
# funkcije koja se takođe prosleđuje kao parametar. Zabranjeno je korišdenje petlji (osim u
# comprehension sintaksi).
# Primer: izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z) = [7, 11, 43]


def izracunaj(lista, fja):

    final_list = [fja(x,y,z) for x,y,z in zip(lista, lista[1:], lista[2:])]

    print(final_list)


izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z)