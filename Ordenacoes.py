# Obtido através da clonagem do repositório github: https://github.com/wschratzenstaller/ordenacao.git
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
