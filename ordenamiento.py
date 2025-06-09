import time

#Bubble Sort (Ordenamiento por burbuja):
def ordenamiento_bubble(distancias):
    tiempo_inicio = time.time() #Marca el tiempo de inicio 
    n = len(distancias)
    for i in range(n): #Recorre la lista n veces
        for j in range(0, n - i - 1):#Compara cada elemento con el siguiente
            if distancias[j][1] > distancias[j + 1][1]:#Condicion de ordenamiento: Si el elemento actual es mayor que el siguiente, los intercambia.
                distancias[j], distancias[j + 1] = distancias[j + 1], distancias[j]
    tiempo_fin = time.time() #Marca el tiempo final
    tiempo_total = tiempo_fin - tiempo_inicio #Calcula el tiempo total de ejecucion
    print(f"Tiempo del ordenamiento por burbuja: {tiempo_total}")
    return distancias #Devuelve la lista ordenada por bubble sort

#Quick Sort (Ordenamiento rápido):
def ordenamiento_quick(distancias):
    tiempo_inicio = time.time() #Marca el tiempo de inicio
    def quick_sort(lista):
        if len(lista) <= 1: #Si la lista tiene un solo elemento o está vacía, ya está ordenada
            return lista
        else:
            pivot = lista[len(lista) // 2] #Elige el pivote como el elemento del medio
            menores = [x for x in lista if x[1] < pivot[1]] #Elementos menores que el pivote
            iguales = [x for x in lista if x[1] == pivot[1]] #Elementos iguales al pivote
            mayores = [x for x in lista if x[1] > pivot[1]] #Elementos mayores que el pivote
            return quick_sort(menores) + iguales + quick_sort(mayores) #Recursión para ordenar los sublistas
    resultado = quick_sort(distancias)
    tiempo_fin = time.time() #Marca el tiempo final
    tiempo_total = tiempo_fin - tiempo_inicio #Calcula el tiempo total de ejecuccion.
    print(f"Tiempo del ordenamiento rápido: {tiempo_total}")
    return resultado #Devuelve la lista ordenada por quick sort


#Selection Sort (Ordenamiento por selección):
def ordenamiento_seleccion(distancias):
    tiempo_inicio = time.time()         # Marca el tiempo de inicio
    n = len(distancias)
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la parte no ordenada de la lista
        minimo = i
        for j in range(i + 1, n):
            if distancias[j][1] < distancias[minimo][1]:
                minimo = j
        # Intercambia el mínimo encontrado con el primer elemento
        distancias[i], distancias[minimo] = distancias[minimo], distancias[i]
    tiempo_fin = time.time()        # Marca el tiempo de fin
    tiempo_total = tiempo_fin - tiempo_inicio  # Calcula el tiempo total de ejecución
    print(f"Tiempo del ordenamiento por selección: {tiempo_total}")
    return distancias               #Devuelve la lista ordenada por selección


#Insertion Sort (Ordenamiento por inserción):
def ordenamiento_insercion(distancias):
    tiempo_inicio = time.time()        # Marca el tiempo de inicio
    for i in range(1, len(distancias)):
        clave = distancias[i]
        j = i - 1
        # Mueve los elementos de distancias[0..i-1], que son mayores que clave, a una posición adelante de su posición actual
        while j >= 0 and clave[1] < distancias[j][1]:
            distancias[j + 1] = distancias[j]
            j -= 1
        distancias[j + 1] = clave
    tiempo_fin = time.time()        # Marca el tiempo de fin
    tiempo_total = tiempo_fin - tiempo_inicio  
    print(f"Tiempo del ordenamiento por inserción: {tiempo_total}")
    return distancias               #Devuelve la lista ordenada por inserción
