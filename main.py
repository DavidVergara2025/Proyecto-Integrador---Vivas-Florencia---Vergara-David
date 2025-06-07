
import random
import math
import funciones

n = int(input("Ingrese la cantidad de lugares a generar: \n"))
destinos = funciones.generar_destinos(n)

if n < 20:
    print(destinos)
else:
    print("La lista fue guardada pero es demasiado extensa para mostrarla por pantalla")

base = funciones.elegir_base(destinos)
print(f"Lugar elegido : {base}")

distancias = funciones.calcular_distancia(destinos, base)
print(distancias)




