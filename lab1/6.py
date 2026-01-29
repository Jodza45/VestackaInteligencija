def razlika(lista1, lista2):

    nova_lista = [x for x in lista1 if x not in lista2]

    return nova_lista


result = razlika([1, 4, 6, "2", "6"], [4, 5, "2"])
print(result)