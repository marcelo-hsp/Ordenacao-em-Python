from functools import partial
from threading import Thread
import time

from listaAleatoria import listaAleatoria
from Ordenacoes import bubble_sort, insertion_sort, selection_sort
from timerCalculator import TempoDeExecucaoDeUmaThread


if __name__ == "__main__":
    lista = listaAleatoria()
    threadBubbleSort = Thread(target=partial(bubble_sort, lista))
    threadInsertionSort = Thread(target=partial(insertion_sort, lista))
    threadSelectionSort = Thread(target=partial(selection_sort, lista))
    TempoDeExecucaoDeUmaThread(threadSelectionSort)
    TempoDeExecucaoDeUmaThread(threadInsertionSort)
    TempoDeExecucaoDeUmaThread(threadBubbleSort)

