def busca_binaria(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return None
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == item: 
        return meio
    elif lista[meio] > item:
        return busca_binaria(lista, item, inicio, meio - 1)  
    else:
        return busca_binaria(lista, item, meio + 1, fim)  

print(busca_binaria([1, 3, 5, 7, 9], 7))  