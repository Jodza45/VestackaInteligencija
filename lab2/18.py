# 18. Korišdenjem programskog jezika Python, napisati funkciju brojevi, koja iz stringa izvlači listu svih
# brojeva koji se u njemu nalaze. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
# Primer: brojevi("42+10=52;10*10=100") = [ 42, 10, 52, 10, 10, 100 ]

import re


def brojevi(tekst):

    lista = [int(x) for x in re.findall(r"(\d+)", tekst)]

    print(lista)


brojevi("42+10=52;10*10=100")