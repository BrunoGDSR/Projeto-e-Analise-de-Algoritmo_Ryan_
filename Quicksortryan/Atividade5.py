# Atividade 5: Eliminando o Risco de Stack Overflow (Quicksort Iterativo)

# Se o Quicksort cair no seu pior caso em um array muito grande, a profundidade da recursão causará um erro de estouro de pilha (Stack Overflow ou RecursionError).
# Tarefa: Implemente o Quicksort de forma 100% iterativa, sem usar recursão. Você deverá simular a Pilha de Chamadas do sistema usando uma estrutura de dados de Pilha (Stack) gerenciada por você mesmo no código (em Python, uma list comum com .append() e .pop(); em TypeScript, um Array com .push() e .pop()). O algoritmo deve armazenar os índices iniciais e finais (low e high) das partições pendentes nessa pilha.


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterativo(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        l, h = stack.pop()
        if l < h:
            pi = partition(arr, l, h)
            if pi - 1 > l:
                stack.append((l, pi - 1))
            if pi + 1 < h:
                stack.append((pi + 1, h))

import random

arr = [random.randint(1, 100) for _ in range(20)]
print("Array original:", arr)
quicksort_iterativo(arr, 0, len(arr) - 1)
print("Array ordenado:", arr)