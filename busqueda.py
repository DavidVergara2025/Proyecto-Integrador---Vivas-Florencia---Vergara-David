import time

def busqueda_lineal(distancias, lugar):
    tiempo_inicio = time.time()
    cont = 0
    for i in distancias:
        cont += 1
        if i[0].lower() == f"lugar {lugar}":
            tiempo_fin = time.time()
            tiempo_total = tiempo_fin - tiempo_inicio
            print(f"Distancia hasta {i[0]}: {i[1]}")
            print(f"Posición en el ranking de distancias: {cont}")
            print(f"Tiempo de búsqueda lineal: {tiempo_total}")
            return i
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    print(f"Tiempo de búsqueda lineal: {tiempo_total}")
    print(f"{lugar} no se encuentra en la lista.")
    return None
    
    #Busqueda binaria de distancias. Devuelve el lugar mas cercano a la distancia elegida
def binaria_mas_cercano(lista_ordenada, objetivo, destinos):
    tiempo_inicio = time.time() #Inicia el temporizador   
    #Índices para el inicio y fin de la busqueda
    izquierda = 1  # Empezamos desde el segundo elemento, para exceptuar al lugar propio
    derecha = len(lista_ordenada) - 1
    mejor = lista_ordenada[1]  #inicia con el primer elemento de la lista
    mejor_dif = abs(lista_ordenada[1][1] - objetivo) #diferencia inicial
    #Comienza la busqueda binaria
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  #Se calcula el punto medio
        actual = lista_ordenada[medio]   #Elemento central
        dif = abs(actual[1] - objetivo)     #Diferencia con el objetivo del usuario
        if dif < mejor_dif: #Si la diferencia es menor, se actualiza el valor
            mejor = actual
            mejor_dif = dif
        #Si el valor es menor al objetivo, buscamos en la mitad derecha. Sino en la izquierda
        if actual[1] < objetivo:
            izquierda = medio + 1
        elif actual[1] > objetivo:
            derecha = medio - 1
        else:
            # Coincidencia exacta: salimos del bucle
            mejor = actual
    # Fin del cronómetro
    tiempo_total = time.time() - tiempo_inicio
    # Mostrar resultados
    nombre, distancia = mejor
    print(f"\n\n==BUSQUEDA BINARIA==\nResultado más cercano encontrado:")
    print(f"Lugar: {nombre}")
    for destino in destinos:
        if destino['Lugar'] == nombre:
            print(f"Coordenadas: x = {destino['x']}, y = {destino['y']}")
    print(f"Distancia encontrada: {distancia:.2f}")
    print(f"Diferencia con la distancia buscada: {abs(distancia - objetivo):.2f}")
    print(f"Tiempo de búsqueda binaria (más cercano): {tiempo_total:.6f} segundos\n")
    return mejor

    #Busqueda lineal de distancias. Devuelve el lugar mas cercano a la distancia elegida
def lineal_mas_cercano(lista, base, objetivo, destinos): 
    lugar_propio = base["Lugar"].strip().lower()  # Obtenemos el nombre del lugar propio
    tiempo_inicio = time.time()  # Inicia el cronómetro  
    mejor = None
    mejor_dif = float('inf')
    # Recorre la lista excluyendo el lugar propio por nombre
    for lugar, distancia in lista:
        if lugar.strip().lower() == lugar_propio:
            continue
        dif = abs(distancia - objetivo)
        if dif < mejor_dif:
            mejor = (lugar, distancia)
            mejor_dif = dif  
    tiempo_total = time.time() - tiempo_inicio  # Fin del cronómetro
    if mejor:
        nombre, distancia = mejor
        print(f"\n\n==BUSQUEDA LINEAL==\nResultado más cercano encontrado:")
        print(f"Lugar: {nombre}")
        for destino in destinos:
            if destino['Lugar'] == nombre:
                print(f"Coordenadas: x = {destino['x']}, y = {destino['y']}")
        print(f"Distancia encontrada: {distancia:.2f}")
        print(f"Diferencia con la distancia buscada: {abs(distancia - objetivo):.2f}")
        print(f"Tiempo de búsqueda lineal (más cercano): {tiempo_total:.6f} segundos\n")
    else:
        print("\nNo se encontró ningún lugar distinto al propio.\n")
    return mejor

