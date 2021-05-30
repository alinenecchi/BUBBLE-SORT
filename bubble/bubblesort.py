# Vídeo "Bubble Sort": https://youtu.be/GiNPe_678Ms
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
    print (final_time)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)
