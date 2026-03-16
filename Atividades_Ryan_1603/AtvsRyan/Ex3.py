def max_lista(lista):
    if len(lista) == 1:  
        return lista[0]
    maior_do_resto = max_lista(lista[1:])  
    return lista[0] if lista[0] > maior_do_resto else maior_do_resto

print(max_lista([3, 7, 2, 9, 5])) 