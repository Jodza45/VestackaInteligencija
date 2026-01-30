def zamena(lista, x):

    final_list = [sum(lista[i + 1:]) if j < x else j for i, j in enumerate(lista)]

    print(final_list)


zamena([1, 7, 5, 4, 9, 1, 2, 7], 5)