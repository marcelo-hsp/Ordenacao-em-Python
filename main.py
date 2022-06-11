from functools import partial
from threading import Thread
import time

from listaAleatoria import listaAleatoria
from Ordenacoes import bubble_sort, insertion_sort, selection_sort

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

