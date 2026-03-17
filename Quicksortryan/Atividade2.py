# Atividade 2: Guerra dos Pivôs (Análise de Desempenho)

# Escreva três funções de particionamento diferentes para o seu Quicksort:1. Pivô sendo o primeiro elemento.
# 2. Pivô sendo um elemento aleatório.
# 3. Pivô sendo a Mediana de Três (escolher o primeiro, o do meio e o último elemento do array, e usar o valor do meio entre os três como pivô).

# Tarefa: Gere um array de 10.000 números que já esteja totalmente ordenado de forma decrescente. Meça e exiba o tempo de execução de cada uma das três abordagens para ordenar esse mesmo array. Escreva um pequeno parágrafo no código (em forma de comentário) explicando os resultados baseados na teoria do Pior Caso do Quicksort.

import random
import time

def partition_first(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def partition_random(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition_lomuto(arr, low, high)

def partition_median_of_three(arr, low, high):
    mid = (low + high) // 2
    candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    candidates.sort(key=lambda x: x[0])
    median_index = candidates[1][1]
    arr[high], arr[median_index] = arr[median_index], arr[high]
    return partition_lomuto(arr, low, high)

def partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, partition_func):
    if low < high:
        pi = partition_func(arr, low, high)
        quicksort(arr, low, pi - 1, partition_func)
        quicksort(arr, pi + 1, high, partition_func)

def measure_time(arr, partition_func):
    arr_copy = arr[:] 
    start = time.time()
    quicksort(arr_copy, 0, len(arr_copy) - 1, partition_func)
    end = time.time()
    return end - start

arr = list(range(10000, 0, -1))

# Medindo tempos
time_first = measure_time(arr, partition_first)
time_random = measure_time(arr, partition_random)
time_median = measure_time(arr, partition_median_of_three)

print(f"Tempo com pivô primeiro elemento: {time_first:.4f} segundos")
print(f"Tempo com pivô aleatório: {time_random:.4f} segundos")
print(f"Tempo com pivô mediana de três: {time_median:.4f} segundos")

