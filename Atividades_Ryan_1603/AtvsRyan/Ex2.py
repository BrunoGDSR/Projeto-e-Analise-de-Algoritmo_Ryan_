def contar_itens(lista):
    if lista == []: 
        return 0
    return 1 + contar_itens(lista[1:])  

print(contar_itens([1, 2, 3, 4, 5]))  