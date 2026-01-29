import itertools


def izmeni1(lista):

    nova_lista = []

    for i, x in enumerate(lista):
        nova_lista.append(sum(lista[0:(i+1)]))

    return nova_lista


def izmeni2(lista):

    nova_lista = [sum(lista[:(i+1)]) for i, x in enumerate(lista)]

    return nova_lista



def izmeni3(lista):

    return list(itertools.accumulate(lista))


result = izmeni3([1, 2, 4, 7, 9])
print(result)