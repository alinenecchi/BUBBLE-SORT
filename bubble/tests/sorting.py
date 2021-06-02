import timeit

def bubble_sort(lista):
    start_time = timeit.default_timer()
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
    final_time = timeit.default_timer() - start_time
    return final_time
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

def insertion_sort(lista):
    start_time = timeit.default_timer()
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave
    final_time = timeit.default_timer() - start_time
    return final_time
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

def selection_sort(lista):
    start_time = timeit.default_timer()
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    final_time = timeit.default_timer() - start_time
    return final_time
# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

def quick_sort(lista, inicio=0, fim=None):
    start_time = timeit.default_timer()
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quick_sort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quick_sort(lista, p+1, fim)
    final_time = timeit.default_timer() - start_time
    return final_time

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def merge_sort(lista, inicio=0, fim=None):
    start_time = timeit.default_timer()
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    final_time = timeit.default_timer() - start_time
    return final_time

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
