def numlista(*lista_podataka):
    stringovi = [x for x in lista_podataka if (type(x).__name__ == "str")]
    integeri = [x for x in lista_podataka if (type(x).__name__ == "int")]
    floatovi = [x for x in lista_podataka if (type(x).__name__ == "float")]
    lista = [x for x in lista_podataka if (type(x).__name__ == "list")]

    return {'Stringovi ': stringovi, 'Integer ': integeri, "Floatovi ": floatovi, "Liste ": lista}


def numlistarecnik(*lista_podataka):
    recnik = {}

    for x in lista_podataka:
        tip = type(x)
        tip_formatirano = tip.__name__

        if tip_formatirano not in recnik:
            recnik[tip_formatirano] = []

        recnik[tip_formatirano].append(x)

    return recnik


rezultat = numlistarecnik("Jovan", "Jovana", "Konstantin", 1, 1.2, 5.4, "Petar", [1,2,3,4,5,6], [12,34,56,78])
print(rezultat)