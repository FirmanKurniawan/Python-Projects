def intersecao_listas(lista1, lista2):
    lista = []
    for x in range(len(lista2)):
        for c in range(len(lista1)):
            if lista2[x] != lista1[c]:
                lista.append(c)
    return lista
