from random import *

def listaAleatoria():
    lista_aleatoria = []
    for i in range(0, 1000, 1):
        lista_aleatoria.append(randint(-10000, 10000))
    return lista_aleatoria
