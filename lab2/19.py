# 19. Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja broji koliko karaktera se
# ponavlja uzastopno više puta u prosleđenom stringu. Zabranjeno je korišdenje petlji (osim u
# comprehension sintaksi).
# Primer: izbaci("aatesttovi") = 2


import itertools

def izbaci(tekst):

    broj = len([k for k, g in itertools.groupby(tekst) if len(list(g)) > 1])
    print(broj)

izbaci("aateestttovi")