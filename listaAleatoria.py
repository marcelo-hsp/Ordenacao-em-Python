from random import *

def listaAleatoria():
    try:
        lista_aleatoria = []
        for i in range(0, 10000, 1):
            valor = randint(1, 100000)
            if valor in lista_aleatoria:
                while valor in lista_aleatoria:
                    valor = randint(1, 100000)
            lista_aleatoria.append(valor)
    except Exception as ex:
        raise("Algo ocorreu", ex)
    return lista_aleatoria
