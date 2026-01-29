def brojanje(recnik):

    lista_tipova = []
    lista_tuplova = []

    for x in recnik.values():
        if (type(x)).__name__ not in lista_tipova:
            lista_tipova.append((type(x)).__name__)
            tip = (type(x)).__name__
            count = 0
            for y in recnik.values():
                if (type(y)).__name__ == tip:
                    count += 1
            tupl = (f'{tip}: ', count)
            lista_tuplova.append(tupl)

    return lista_tuplova
    

result = brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8})
print(result) 
            