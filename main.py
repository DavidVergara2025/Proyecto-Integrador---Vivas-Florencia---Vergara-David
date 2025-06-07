
import random
import math
import funciones

print("""========PROYECTO INTEGRADOR - PROGRAMACIÓN I=========
        2025 - UTN - TUPaD 
        Autores: Vivas, Florencia - Vergara, David
      
        Bienvenido al gestor de distancias entre lugares.
        Este programa genera una lista de lugares con coordenadas aleatorias.
        Luego, el usuario puede elegir uno de ellos para calcular la distancia a los demás puntos.
        A continuación, se ordena la lista mediante distintos métodos de ordenamiento y se permiten realizar búsquedas.
      """)

n = int(input("Ingrese la cantidad de lugares a generar: \n"))
destinos = funciones.generar_destinos(n)

if n < 20:
    for i in destinos:
        print(f"Lugar: {i['Lugar']}, Coordenadas: ({i['x']}, {i['y']})")  # Muestra cada lugar con sus coordenadas
else:
    print("La lista fue guardada pero es demasiado extensa para mostrarla por pantalla")

base = funciones.elegir_base(destinos)
print(f"Lugar elegido : {base}\n")

distancias = funciones.calcular_distancia(destinos, base)
for i in distancias:
    print(f"{i[0]}, Distancia: {i[1]}")  # Muestra el lugar y la distancia calculada desde el lugar elegido

# Ordenamiento de la lista de distancias





