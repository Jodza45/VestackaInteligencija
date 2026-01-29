def izdvoji(lista):
    nova = []
    n = 0

    for i, x in enumerate(lista):
        if n < len(x):
            nova.append(x[n])
        else:
            nova.append(0)
        
        n += 1


    return nova


result = izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]])
print(result)