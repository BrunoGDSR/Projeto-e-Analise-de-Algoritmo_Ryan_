# Atividade 1: Implementação Base e Rastreamento (Tracing)

# Implemente a versão clássica do algoritmo Quicksort escolhendo o último elemento como pivô (Esquema de partição de Lomuto). 
# Para provar que o algoritmo está funcionando como esperado, modifique sua função para que ela imprima o estado do array toda vez que a função de particionamento terminar de rodar, destacando qual foi o pivô utilizado naquela etapa.
# Teste: Crie um array desordenado de 10 números inteiros aleatórios e mostre o passo a passo no console.

import random


def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1       
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    print(f"Partição concluída com pivô {pivot}: {arr}")
    
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [random.randint(1, 100) for _ in range(10)]
print("Array inicial:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Array final ordenado:", arr)