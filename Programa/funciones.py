import random
import math
#Funcion que genera una lista de lugares con coordenadas aleatorias
def generar_destinos(n):
    destinos = []
    for i in range(1, n+1):
        destino = {
            "Lugar" : f"Lugar {i}",
            "x" : random.randint(0, 1000000),
            "y" : random.randint(0, 1000000)
        }
        destinos.append(destino) #Se agrega cada lugar generado con sus coordenadas a la lista destinos
    return destinos

#Devuelve el elemento elegido por el usuario ((Lugar y coordenadas)
def elegir_base(destinos):
    base = int(input("Elija su ubicacion (En numero de 1 a la cantidad elegida) para calcular la distancia a los demas puntos: \n"))
    return destinos[base -1]

#Cálculo de las distancias desde cada punto al elegido por el usuario (con teorema de pitágoras)
def calcular_distancia(destinos, base):
    distancias = []
    par_lugar_distancia = {}
    for i in destinos:
        x2 = i["x"]
        y2 = i["y"]
        x1 = base["x"]
        y1 = base["y"]
        distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        par_lugar_distancia = {i["Lugar"] : distancia}
        distancias.append(par_lugar_distancia)

    return distancias #Devuelve una lista con las distancias desde cada punto




