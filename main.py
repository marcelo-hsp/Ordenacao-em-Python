from functools import partial
from threading import Thread
import time

from listaAleatoria import listaAleatoria
from Ordenacoes import bubble_sort, insertion_sort, selection_sort
from timerCalculator import TempoDeExecucaoDeUmaThread


quantidadeDeExecuções = 10

if __name__ == "__main__":
    lista = listaAleatoria() 
    try:
        fileSelection = open("txtFiles/bubble.txt", "w")
        i = 0
        while i < quantidadeDeExecuções:
            threadBubbleSort = Thread(target=partial(bubble_sort, lista))
            TempoDeExecucaoDeUmaThread(threadBubbleSort, fileSelection)
            i += 1
        fileSelection.close()
    except FileNotFoundError:
        raise("Arquivo não encontrado!")
    time.sleep(1)
    try:
        fileSelection = open("txtFiles/insertion.txt", "w")
        i = 0
        while i < quantidadeDeExecuções:
            threadInsertionSort = Thread(target=partial(insertion_sort, lista))
            TempoDeExecucaoDeUmaThread(threadInsertionSort, fileSelection)
            i += 1
        fileSelection.close()
    except FileNotFoundError:
        raise("Arquivo não encontrado!")
    time.sleep(1)
    try:
        fileSelection = open("txtFiles/selection.txt", "w")
        i = 0
        while i < quantidadeDeExecuções:
            threadSelectionSort = Thread(target=partial(selection_sort, lista))
            TempoDeExecucaoDeUmaThread(threadSelectionSort, fileSelection)
            i += 1
        fileSelection.close()
    except FileNotFoundError:
        raise("Arquivo não encontrado!")
    

