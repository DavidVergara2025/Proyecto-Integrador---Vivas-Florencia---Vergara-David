import time
#Bubble Sort (Ordenamiento por burbuja):

#Quick Sort (Ordenamiento rápido):

#Selection Sort (Ordenamiento por selección):
def ordenamiento_seleccion(distancias):
    tiempo_inicio = time.time()  # Marca el tiempo de inicio
    n = len(distancias)
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la parte no ordenada de la lista
        minimo = i
        for j in range(i + 1, n):
            if distancias[j][1] < distancias[minimo][1]:
                minimo = j
        # Intercambia el mínimo encontrado con el primer elemento
        distancias[i], distancias[minimo] = distancias[minimo], distancias[i]
    tiempo_fin = time.time()  # Marca el tiempo de fin
    tiempo_total = tiempo_fin - tiempo_inicio  # Calcula el tiempo total de ejecución
    print(f"Tiempo del ordenamiento por selección: {tiempo_total}")
    return distancias

#Insertion Sort (Ordenamiento por inserción):
