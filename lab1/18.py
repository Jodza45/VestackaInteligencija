def kreiraj(lista):
    
    return [[x for x in prva if x not in druga] for prva, druga in zip(lista, lista[1:])]


result = kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]])
print(result)