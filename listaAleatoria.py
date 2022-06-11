from random import *

def listaAleatoria():
    lista_aleatoria = []
    for i in range(-1000, 1000, 1):
        lista_aleatoria.append(randint(-10000, 10000))
    return lista_aleatoria
