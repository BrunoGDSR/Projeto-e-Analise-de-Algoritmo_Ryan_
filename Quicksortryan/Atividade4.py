# Atividade 4: Hibridização (Quicksort + Insertion Sort)

# O Quicksort perde eficiência devido ao overhead da recursão quando os subarrays ficam muito pequenos (ex: menores que 10 ou 15 elementos). Para arrays pequenos, o Insertion Sort (Ordenação por Inserção) é mais rápido.
# Tarefa: Implemente o Insertion Sort. Em seguida, modifique o seu Quicksort para que, quando o tamanho da partição atual for menor ou igual a 10 elementos, ele pare de chamar o Quicksort recursivamente e chame o Insertion Sort apenas para aquele pedaço do array. Compare o tempo dessa versão híbrida com o Quicksort puro da Atividade 1 em um array de 50.000 elementos aleatórios.

import random
import time

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_puro(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_puro(arr, low, pi - 1)
        quicksort_puro(arr, pi + 1, high)

def quicksort_hibrido(arr, low, high):
    if high - low + 1 <= 10:
        insertion_sort(arr, low, high)
    elif low < high:
        pi = partition(arr, low, high)
        quicksort_hibrido(arr, low, pi - 1)
        quicksort_hibrido(arr, pi + 1, high)

arr = [random.randint(1, 100000) for _ in range(50000)]

arr_copy1 = arr[:]
start = time.time()
quicksort_puro(arr_copy1, 0, len(arr_copy1) - 1)
end = time.time()
print(f"Tempo Quicksort puro: {end - start:.4f} segundos")

arr_copy2 = arr[:]
start = time.time()
quicksort_hibrido(arr_copy2, 0, len(arr_copy2) - 1)
end = time.time()
print(f"Tempo Quicksort híbrido: {end - start:.4f} segundos")

