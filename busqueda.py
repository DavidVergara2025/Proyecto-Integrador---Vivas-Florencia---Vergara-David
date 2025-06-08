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