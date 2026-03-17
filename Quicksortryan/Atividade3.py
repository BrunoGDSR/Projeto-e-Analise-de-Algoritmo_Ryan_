# Atividade 3: Quicksort no Mundo Real (Ordenação de Objetos)

# Crie uma classe ou interface Funcionario contendo nome (string), salario (float/number) e idade (int/number).
# Crie um array com pelo menos 15 funcionários fictícios.
# Tarefa: Adapte o seu Quicksort para receber uma função de comparação (custom comparator). Use o Quicksort para ordenar a lista de funcionários com as seguintes regras de prioridade:
# 1. Ordenar por salário de forma decrescente (do maior para o menor).
# 2. Em caso de empate no salário, ordenar por nome em ordem alfabética (crescente).

class Funcionario:
    def __init__(self, nome, salario, idade):
        self.nome = nome
        self.salario = salario
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} - Salário: {self.salario}, Idade: {self.idade}"

def partition(arr, low, high, comparator):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if comparator(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, comparator):
    if low < high:
        pi = partition(arr, low, high, comparator)
        quicksort(arr, low, pi - 1, comparator)
        quicksort(arr, pi + 1, high, comparator)

def comparator_funcionario(a, b):
    if a.salario > b.salario:
        return True
    elif a.salario < b.salario:
        return False
    else:
        return a.nome < b.nome

funcionarios = [
    Funcionario("Ana", 5000, 30),
    Funcionario("Bruno", 7000, 40),
    Funcionario("Carlos", 7000, 25),
    Funcionario("Daniela", 4500, 28),
    Funcionario("Eduardo", 6000, 35),
    Funcionario("Fernanda", 5000, 32),
    Funcionario("Gabriel", 8000, 45),
    Funcionario("Helena", 5500, 29),
    Funcionario("Igor", 4000, 26),
    Funcionario("Joana", 7000, 38),
    Funcionario("Kleber", 3000, 22),
    Funcionario("Larissa", 6000, 33),
    Funcionario("Marcos", 5000, 31),
    Funcionario("Natália", 7000, 27),
    Funcionario("Otávio", 6500, 36)
]

print("Lista original:")
for f in funcionarios:
    print(f)

quicksort(funcionarios, 0, len(funcionarios) - 1, comparator_funcionario)

print("\nLista ordenada:")
for f in funcionarios:
    print(f)