def spojidict(lista1, lista2):

    N = None
    if len(lista1) > len(lista2):
        N = len(lista1)
        lista2 += ['-'] * N
    else:
        N = len(lista2)
        lista1 += ['-'] * N

    final_list_dict = [{"prva: ": x, "druga: ": y} for x,y in zip(lista1, lista2)]

    print(final_list_dict)


spojidict([1, 7, 2, 4], [2, 5, 2])    