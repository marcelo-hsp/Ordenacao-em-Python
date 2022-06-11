from functools import partial
from threading import Thread
import time

from listaAleatoria import listaAleatoria

def bubble_sort(valores):
    n = len(valores)-1
    for i in range(n,0,-1):
        for j in range(n):
            if valores[j] > valores[j + 1]:
                auxiliar = valores[j]
                valores[j] = valores[j + 1]
                valores[j + 1] = auxiliar
    return 0

def insertion_sort(valores):
    n = len(valores)
    for i in range(1, n, +1):
        chave = valores[i]
        j = i - 1
        while (j > -1 and valores[j] > chave):
            valores[j+1] = valores[j]
            j -= 1
        valores[j+1] = chave
    return 0

def selection_sort(valores):
    n = len(valores)
    for i in range(0, n-1, +1):
        menor = i
        for j in range(i+1, n, +1):
            if (valores[j] < valores[menor]):
                menor = j
        auxiliar = valores[i]
        valores[i] = valores[menor]
        valores[menor] = auxiliar
    return 0

def TempoDeExecucaoDeUmaThread(thr: Thread):
    t1 = time.time()
    thr.start()
    t2 = time.time()
    print(str(t2 - t1))

lista = listaAleatoria()

threadBubbleSort = Thread(target=partial(bubble_sort, lista))
threadInsertionSort = Thread(target=partial(insertion_sort, lista))
threadSelectionSort = Thread(target=partial(selection_sort, lista))


TempoDeExecucaoDeUmaThread(threadSelectionSort)
TempoDeExecucaoDeUmaThread(threadInsertionSort)
TempoDeExecucaoDeUmaThread(threadBubbleSort)

