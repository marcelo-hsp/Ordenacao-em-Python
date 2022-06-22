from random import *

v_min = 40000
v_max = 40000

def listaAleatoria():
    try:
        lista_aleatoria = []
        for i in range(0, 10000, 1):
            valor = randint(1, 100000)
            lista_aleatoria.append(valor)
    except Exception as ex:
        raise("Algo ocorreu", ex)
    return lista_aleatoria
