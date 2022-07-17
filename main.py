from functools import partial
from threading import Thread

from listaAleatoria import listaAleatoria
from Ordenacoes import bubble_sort, insertion_sort, selection_sort
from timerCalculator import TempoDeExecucaoDeUmaThread


quantidadeDeExecuções = 1

if __name__ == "__main__":
    try:
        file = open("./vetorDesordenado.txt", "r") ## r=read
        lines = file.readlines()
    except FileNotFoundError as error:
        print("Erro1: Arquivo não encontrado: %s" % error)
    except IOError as error:
        print("Erro2: Erro de entrada e saída: %s" % error)
    except Exception as ex:
        print("Erro3: Erro inexperado: %s" % ex)

    lista = []
    for line in lines:
        lista.append(int(line))
    
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
    

