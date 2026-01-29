def izmeni(lista):
    
    pp = [x + 1 for i, x in enumerate(lista) if i % 2 == 0]

    np = [x - 1 for i, x in enumerate(lista) if i % 2 != 0]

    return {'pp': pp, 'np': np}



result = izmeni([8, 6, 3, 1, 1])
print(result)    