def razlika(lista):
    pom_lista = lista
    lista_parova = list(zip(lista, pom_lista[1:]))

    nova_lista = [x - y for x, y in lista_parova]

    return nova_lista


result = razlika([8, 5, 3, 1, 1])
print(result)