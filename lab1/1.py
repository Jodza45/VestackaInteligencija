def parni1(*lista_brojeva):
    parni_brojevi = [x for x in lista_brojeva if x % 2 == 0]

    neparni_brojevi = [x for x in lista_brojeva if x % 2 != 0]

    return {'Parni: ': parni_brojevi, 'Neparni: ': neparni_brojevi}

def parni2(*lista_brojeva):
    parni_brojevi = []
    neparni_brojevi = []

    for x in lista_brojeva:
        if(x % 2 == 0):
            parni_brojevi.append(x)
        else:
            neparni_brojevi.append(x)

    return {'Parni: ': parni_brojevi, 'Neparni': neparni_brojevi}


rezultat = parni2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(rezultat)