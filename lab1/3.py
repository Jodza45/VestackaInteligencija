import operator

def uredi(lista_brojeva, N, num):
    if len(lista_brojeva) <= N:
        return "Nema dovoljno elemenata"
    
    for x in lista_brojeva:
        index = lista_brojeva.index(x)
        if(index < N):
            lista_brojeva[index] += num
        else:
            lista_brojeva[index] -= num

    return lista_brojeva



def uredi2(lista_brojeva, N, num):
    nova_lista = []

    for i in range(len(lista_brojeva)):
        if i < N:
            nova_lista.append(i + num)
        else:
            nova_lista.append(i - num)

    return nova_lista



def uredi3(lista_brojeva, N, num):
    nova_lista = []

    for i, x in enumerate(lista_brojeva):
        if i < N:
            nova_lista.append(x + num)
        else:
            nova_lista.append(x - num)
    
    return nova_lista




result = uredi3([1,2,3,4,5,6,7,8,9,10], 5, 2)
print(result)